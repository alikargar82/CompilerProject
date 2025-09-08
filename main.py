from antlr4 import *
import argparse
from CustomCourseListener import CustomCourseListener
from code_generator import ContentAwareCourseCodeGenerator
from gen.CourseLexer import CourseLexer
from gen.CourseParser import CourseParser
from required_code_collection.ast_to_networkx_graph import show_ast

def main(arguments):
	import os
	stream = FileStream(arguments.input, encoding='utf8')
	lexer = CourseLexer(stream)
	token_stream = CommonTokenStream(lexer)
	parser = CourseParser(token_stream)
	parse_tree = parser.courseFile()
	
	# Get the directory of the input file to resolve relative references
	base_path = os.path.dirname(os.path.abspath(arguments.input))
	ast_builder_listener = CustomCourseListener(base_path)
	
	ast_builder_listener.rule_names = parser.ruleNames
	walker = ParseTreeWalker()
	walker.walk(t=parse_tree, listener=ast_builder_listener)
	ast = ast_builder_listener.ast
	show_ast(ast.root)
	traversal = ast.traverse_ast(ast.root)
	print("AST Traversal:")
	print(traversal)
	
	# Generate course-specific Python code with embedded content
	code_gen = ContentAwareCourseCodeGenerator()
	final_code = code_gen.generate_from_ast(traversal)
	print("\nGenerated Code:")
	print(final_code[:1000] + "..." if len(final_code) > 1000 else final_code)
	
	# Write the generated code to the specified output file
	with open('generated_code.py', 'w', encoding='utf-8') as mcp_output:
		mcp_output.write(final_code)
		
	print("\nCode generated successfully! Check 'generated_course.py' and 'generated_code.py'")


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'input/main.json')
	argparser.add_argument('-o', '--output', help='Output path', default=r'output/output.py')
	args = argparser.parse_args()
	main(args)
