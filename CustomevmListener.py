from gen.evmListener import evmListener
from gen.evmParser import evmParser
from required_code_collection.ast import AST
from required_code_collection.make_ast_subtree import make_ast_subtree

class CustomevmListener(evmListener):
	def __init__(self):
		self.overridden_rules = ['program','print_variable','for_increment','params','func_body','condition'] #change
		self.binary_operator_list = ['term','expression','variable_assignment','comparison_statement'] #change
		self.compound_rules = ['switch_statement','block_statement','case_statement','default_case','if_statement'] #change
		self.scoped_rules = ['block_statement','if_statement','case_statement','switch_statement','default_case'] #change
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