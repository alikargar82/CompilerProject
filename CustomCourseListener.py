from gen.CourseListener import CourseListener
from gen.CourseParser import CourseParser
from gen.CourseLexer import CourseLexer
from antlr4 import *
from required_code_collection.ast import AST
from required_code_collection.make_ast_subtree import make_ast_subtree
import os

class CustomCourseListener(CourseListener):
	def __init__(self, base_path=""):
		self.overridden_rules = ['courseFile', 'object', 'array', 'pair']
		self.binary_operator_list = []
		self.compound_rules = []  # We'll handle compounds manually now
		self.scoped_rules = []    # We'll handle scoping manually now
		self.rule_names = []
		self.ast = AST()
		self.base_path = base_path  # Base path for resolving relative file references
		
		# Meaningful course structure elements
		self.course_metadata_keys = ['name', 'author', 'description', 'level', 'tags']
		self.student_data_keys = ['roster_file', 'capacity', 'classes_file', 'enrollment_mode']
		self.flow_keys = ['type', 'ref', 'modes']
		self.content_keys = ['type', 'title', 'body', 'url', 'transcript', 'duration', 'src', 'caption', 'language', 'code', 'explanation']
		self.question_keys = ['type', 'question', 'options', 'answer', 'hint', 'explanation', 'word_count', 'keyword', 'language', 'starter_code', 'tests']
		self.settings_keys = ['passing_score', 'randomize_questions', 'attempts_allowed', 'time_limit', 'weight']
		self.material_keys = ['type', 'title', 'path', 'url', 'description']
		self.test_keys = ['input', 'expected_output']
		
		# Top-level course structure keys that should become container nodes
		self.course_structure_keys = ['student_data', 'flow', 'content', 'objectives', 'questions', 'settings', 'materials', 'summary']
		
		# Keys that represent collections/arrays that should become container nodes
		self.collection_keys = ['flow', 'content', 'objectives', 'questions', 'materials', 'options', 'tests', 'tags']


	def parse_referenced_file(self, file_path):
		"""Parse a referenced file and return its AST"""
		try:
			# Resolve the full path
			full_path = os.path.join(self.base_path, file_path)
			
			# Create lexer and parser for the referenced file
			stream = FileStream(full_path, encoding='utf8')
			lexer = CourseLexer(stream)
			token_stream = CommonTokenStream(lexer)
			parser = CourseParser(token_stream)
			
			# Parse the referenced file (it should be just an object, not a full courseFile)
			parse_tree = parser.value()  # Use value instead of object
			
			# Create a new listener for this file
			ref_listener = CustomCourseListener(self.base_path)
			ref_listener.rule_names = parser.ruleNames
			
			# Walk the parse tree
			walker = ParseTreeWalker()
			walker.walk(t=parse_tree, listener=ref_listener)
			
			return ref_listener.ast.root
			
		except Exception as e:
			print(f"Error parsing referenced file {file_path}: {e}")
			# Return a simple error node
			return self.ast.make_node(f"error_loading_{file_path}", children=[])


	def exitEveryRule(self, ctx):
		rule_name = self.rule_names[ctx.getRuleIndex()]
		if rule_name not in self.overridden_rules:
			if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
				make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
			else:
				make_ast_subtree(self.ast, ctx, rule_name)


	def exitCourseFile(self, ctx):
		make_ast_subtree(self.ast, ctx, "courseFile", keep_node=True)


	def exitObject(self, ctx):
		# Create a temporary object node but we'll optimize it away later in post-processing
		ctx.compound = True
		make_ast_subtree(self.ast, ctx, "object", keep_node=True)


	def exitArray(self, ctx):
		# Create a temporary array node but we'll optimize it away later in post-processing
		ctx.compound = True
		make_ast_subtree(self.ast, ctx, "array", keep_node=True)


	def exitPair(self, ctx):
		# Extract the key name from the STRING token (remove quotes)
		key_text = ctx.getChild(0).getText()[1:-1]  # Remove surrounding quotes
		value_ctx = ctx.getChild(2)  # The value part of the pair
		
		# Determine the semantic node name
		if key_text in self.course_metadata_keys:
			node_name = f"metadata_{key_text}"
		elif key_text in self.course_structure_keys:
			node_name = key_text
		elif key_text in self.student_data_keys:
			node_name = f"student_{key_text}"
		elif key_text in self.flow_keys:
			node_name = f"flow_{key_text}"
		elif key_text in self.content_keys:
			node_name = f"content_{key_text}"
		elif key_text in self.question_keys:
			node_name = f"question_{key_text}"
		elif key_text in self.settings_keys:
			node_name = f"setting_{key_text}"
		elif key_text in self.material_keys:
			node_name = f"material_{key_text}"
		elif key_text in self.test_keys:
			node_name = f"test_{key_text}"
		elif key_text in ['min', 'max']:
			node_name = f"word_count_{key_text}"
		else:
			# For any other keys, use the key name directly
			node_name = key_text
		
		# Check if this key represents a collection that should be a compound node
		if key_text in self.collection_keys:
			ctx.compound = True
		
		# Special handling for 'ref' keys - load and link the referenced file
		if key_text == 'ref':
			# Get the file path from the value (remove quotes)
			ref_path = value_ctx.getText()[1:-1] if hasattr(value_ctx, 'getText') else str(value_ctx)
			
			# Parse the referenced file and get its AST
			referenced_ast = self.parse_referenced_file(ref_path)
			
			# Create a ref node with the referenced content as children
			ref_node = self.ast.make_node(f"ref_{ref_path.replace('/', '_').replace('.', '_')}", children=[referenced_ast])
			ctx.ast_value = ref_node
			self.ast.root = ref_node
			
		else:
			# Special handling for structural elements
			if key_text in self.course_structure_keys or key_text in self.collection_keys:
				# These become container nodes with compound structure
				ctx.compound = True
				make_ast_subtree(self.ast, ctx, node_name, keep_node=True)
			else:
				# Regular key-value pairs
				make_ast_subtree(self.ast, ctx, node_name, keep_node=True)
