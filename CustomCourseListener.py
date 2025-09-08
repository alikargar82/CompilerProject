from gen.CourseListener import CourseListener
from gen.CourseParser import CourseParser
from required_code_collection.ast import AST
from required_code_collection.make_ast_subtree import make_ast_subtree

class CustomCourseListener(CourseListener):
	def __init__(self):
		self.overridden_rules = [  'tagList'] #change
		self.binary_operator_list = [] #change
		self.compound_rules = [] #change
		self.scoped_rules = [ 'flowItem'] #change
		self.rule_names = []
		self.ast = AST()


	def exitEveryRule(self, ctx):
		rule_name = self.rule_names[ctx.getRuleIndex()]
		if rule_name in self.scoped_rules:
			ctx.compound = True
		if rule_name not in self.overridden_rules:
			if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
				make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
			else:
				make_ast_subtree(self.ast, ctx, rule_name)


# place to define specific functions for grammer rules

def exitCourseFile(self, ctx: CourseParser.CourseFileContext):
	make_ast_subtree(self.ast, ctx, "CourseFile", keep_node=True)

