# Generated from /home/ali/compiler/Course.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by CourseParser#metadata.
    def visitMetadata(self, ctx:CourseParser.MetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#tagList.
    def visitTagList(self, ctx:CourseParser.TagListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#studentData.
    def visitStudentData(self, ctx:CourseParser.StudentDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#flow.
    def visitFlow(self, ctx:CourseParser.FlowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#flowItem.
    def visitFlowItem(self, ctx:CourseParser.FlowItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CourseParser#mode_type.
    def visitMode_type(self, ctx:CourseParser.Mode_typeContext):
        return self.visitChildren(ctx)



del CourseParser