# Generated from /home/ali/compiler/Course.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CourseParser import CourseParser
else:
    from CourseParser import CourseParser

# This class defines a complete listener for a parse tree produced by CourseParser.
class CourseListener(ParseTreeListener):

    # Enter a parse tree produced by CourseParser#courseFile.
    def enterCourseFile(self, ctx:CourseParser.CourseFileContext):
        pass

    # Exit a parse tree produced by CourseParser#courseFile.
    def exitCourseFile(self, ctx:CourseParser.CourseFileContext):
        pass


    # Enter a parse tree produced by CourseParser#metadata.
    def enterMetadata(self, ctx:CourseParser.MetadataContext):
        pass

    # Exit a parse tree produced by CourseParser#metadata.
    def exitMetadata(self, ctx:CourseParser.MetadataContext):
        pass


    # Enter a parse tree produced by CourseParser#tagList.
    def enterTagList(self, ctx:CourseParser.TagListContext):
        pass

    # Exit a parse tree produced by CourseParser#tagList.
    def exitTagList(self, ctx:CourseParser.TagListContext):
        pass


    # Enter a parse tree produced by CourseParser#studentData.
    def enterStudentData(self, ctx:CourseParser.StudentDataContext):
        pass

    # Exit a parse tree produced by CourseParser#studentData.
    def exitStudentData(self, ctx:CourseParser.StudentDataContext):
        pass


    # Enter a parse tree produced by CourseParser#flow.
    def enterFlow(self, ctx:CourseParser.FlowContext):
        pass

    # Exit a parse tree produced by CourseParser#flow.
    def exitFlow(self, ctx:CourseParser.FlowContext):
        pass


    # Enter a parse tree produced by CourseParser#flowItem.
    def enterFlowItem(self, ctx:CourseParser.FlowItemContext):
        pass

    # Exit a parse tree produced by CourseParser#flowItem.
    def exitFlowItem(self, ctx:CourseParser.FlowItemContext):
        pass


    # Enter a parse tree produced by CourseParser#mode_type.
    def enterMode_type(self, ctx:CourseParser.Mode_typeContext):
        pass

    # Exit a parse tree produced by CourseParser#mode_type.
    def exitMode_type(self, ctx:CourseParser.Mode_typeContext):
        pass



del CourseParser