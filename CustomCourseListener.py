from gen.CourseListener import CourseListener
from gen.CourseParser import CourseParser
from required_code_collection.ast import AST
from required_code_collection.make_ast_subtree import make_ast_subtree

class CustomCourseListener(CourseListener):
	def __init__(self):
		self.overridden_rules = ['ref','type','course_intro','courseIntro'] #change
		self.binary_operator_list = [] #change
		self.compound_rules = [] #change
		self.scoped_rules = [] #change
		self.rule_names = []
		self.ast = AST()


	def exitArray(self, ctx: CourseParser.ArrayContext):
		make_ast_subtree(self.ast, ctx, "array", keep_node=True)

	def exitCourseIntro(self, ctx: CourseParser.CourseIntroContext):
		make_ast_subtree(self.ast, ctx, "course_intro", keep_node=True)

	def exitEveryRule(self, ctx):
		rule_name = self.rule_names[ctx.getRuleIndex()]
		if rule_name in self.scoped_rules:
			ctx.compound = True
		if rule_name not in self.overridden_rules:
			if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
				make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
			else:
				make_ast_subtree(self.ast, ctx, rule_name)

	# Specific exit methods for grammar rules to extract structured data
	
	def exitCourseFile(self, ctx: CourseParser.CourseFileContext):
		make_ast_subtree(self.ast, ctx, "CourseFile", keep_node=True)

	def exitCourseIntroduction(self, ctx: CourseParser.CourseIntroductionContext):
		make_ast_subtree(self.ast, ctx, "course_introduction", keep_node=True)

	def exitCourseIntro(self, ctx: CourseParser.CourseIntroContext):
		# Extract metadata from the fixed courseIntro structure
		# Structure: LBRACE "name" COLON STRING COMMA "author" COLON STRING COMMA "description" COLON STRING COMMA "level" COLON STRING COMMA "tags" COLON array RBRACE
		
		# Create children list for the course_intro node
		children = []
		
		# Extract metadata from the fixed structure
		# Child 3: name value, Child 7: author value, Child 11: description value, Child 15: level value
		if ctx.getChildCount() >= 16:
			name_value = ctx.getChild(3).getText()
			author_value = ctx.getChild(7).getText()
			description_value = ctx.getChild(11).getText()
			level_value = ctx.getChild(15).getText()
			
			
			# Create metadata nodes as children
			children.append(self.ast.make_node(f"metadata_name_{name_value}", []))
			children.append(self.ast.make_node(f"metadata_author_{author_value}", []))
			children.append(self.ast.make_node(f"metadata_description_{description_value}", []))
			children.append(self.ast.make_node(f"metadata_level_{level_value}", []))
		
		# Create the course_intro node with metadata as children
		course_intro_node = self.ast.make_node("course_intro", children)
		ctx.ast_value = course_intro_node
		self.ast.root = course_intro_node

	def exitFlow(self, ctx: CourseParser.FlowContext):
		make_ast_subtree(self.ast, ctx, "flow", keep_node=True)

	def exitArrayOfFlowItems(self, ctx: CourseParser.ArrayOfFlowItemsContext):
		make_ast_subtree(self.ast, ctx, "arrayOfFlowItems", keep_node=True)

	def exitFlowItem(self, ctx: CourseParser.FlowItemContext):
		make_ast_subtree(self.ast, ctx, "flowItem", keep_node=True)

	def exitType(self, ctx: CourseParser.TypeContext):
		# Extract the type value (registration, chapter, quiz, exam, resource)
		if ctx.getChildCount() >= 3:  # "type" : "value"
			type_value = ctx.getChild(2).getText()
			make_ast_subtree(self.ast, ctx, f"flow_type_{type_value}", keep_node=True)
		else:
			make_ast_subtree(self.ast, ctx, "type", keep_node=True)

	def exitRef(self, ctx: CourseParser.RefContext):
		# Extract the reference path
		if ctx.getChildCount() >= 4:  # , "ref" : "path"
			ref_path = ctx.getChild(3).getText()  # Child 3 is the actual path
			make_ast_subtree(self.ast, ctx, f"ref_{ref_path}", keep_node=True)
		else:
			make_ast_subtree(self.ast, ctx, "ref", keep_node=True)

	def exitModes(self, ctx: CourseParser.ModesContext):
		make_ast_subtree(self.ast, ctx, "modes", keep_node=True)

	def exitPair(self, ctx: CourseParser.PairContext):
		# Extract key-value pairs for metadata
		if ctx.getChildCount() >= 3:  # "key" : value
			key = ctx.getChild(0).getText().strip('"')
			value = ctx.getChild(2).getText()
			
			# Map specific metadata keys to meaningful tokens
			if key == "name":
				make_ast_subtree(self.ast, ctx, f"metadata_name_{value}", keep_node=True)
			elif key == "author":
				make_ast_subtree(self.ast, ctx, f"metadata_author_{value}", keep_node=True)
			elif key == "description":
				make_ast_subtree(self.ast, ctx, f"metadata_description_{value}", keep_node=True)
			elif key == "level":
				make_ast_subtree(self.ast, ctx, f"metadata_level_{value}", keep_node=True)
			else:
				make_ast_subtree(self.ast, ctx, f"pair_{key}_{value}", keep_node=True)
		else:
			make_ast_subtree(self.ast, ctx, "pair", keep_node=True)

	def exitString(self, ctx):
		# Handle string values in metadata context
		string_value = ctx.getText()
		make_ast_subtree(self.ast, ctx, string_value, keep_node=True)

	def exitArray(self, ctx: CourseParser.ArrayContext):
		make_ast_subtree(self.ast, ctx, "array", keep_node=True)

	def exitValue(self, ctx: CourseParser.ValueContext):
		make_ast_subtree(self.ast, ctx, "value", keep_node=True)

	def exitObject(self, ctx: CourseParser.ObjectContext):
		make_ast_subtree(self.ast, ctx, "object", keep_node=True)

