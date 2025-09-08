# Generated from /home/ali/CompilerProject/Course.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CourseParser import CourseParser
else:
    from CourseParser import CourseParser

# This class defines a complete generic visitor for a parse tree produced by CourseParser.

class CourseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CourseParser#courseFile.
    def visitCourseFile(self, ctx:CourseParser.CourseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#object.
    def visitObject(self, ctx:CourseParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#array.
    def visitArray(self, ctx:CourseParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#pair.
    def visitPair(self, ctx:CourseParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#value.
    def visitValue(self, ctx:CourseParser.ValueContext):
        return self.visitChildren(ctx)



del CourseParser