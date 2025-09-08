# Generated from /home/ali/CompilerProject/Course.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by CourseParser#courseIntroduction.
    def enterCourseIntroduction(self, ctx:CourseParser.CourseIntroductionContext):
        pass

    # Exit a parse tree produced by CourseParser#courseIntroduction.
    def exitCourseIntroduction(self, ctx:CourseParser.CourseIntroductionContext):
        pass


    # Enter a parse tree produced by CourseParser#courseIntro.
    def enterCourseIntro(self, ctx:CourseParser.CourseIntroContext):
        pass

    # Exit a parse tree produced by CourseParser#courseIntro.
    def exitCourseIntro(self, ctx:CourseParser.CourseIntroContext):
        pass


    # Enter a parse tree produced by CourseParser#flow.
    def enterFlow(self, ctx:CourseParser.FlowContext):
        pass

    # Exit a parse tree produced by CourseParser#flow.
    def exitFlow(self, ctx:CourseParser.FlowContext):
        pass


    # Enter a parse tree produced by CourseParser#arrayOfFlowItems.
    def enterArrayOfFlowItems(self, ctx:CourseParser.ArrayOfFlowItemsContext):
        pass

    # Exit a parse tree produced by CourseParser#arrayOfFlowItems.
    def exitArrayOfFlowItems(self, ctx:CourseParser.ArrayOfFlowItemsContext):
        pass


    # Enter a parse tree produced by CourseParser#flowItem.
    def enterFlowItem(self, ctx:CourseParser.FlowItemContext):
        pass

    # Exit a parse tree produced by CourseParser#flowItem.
    def exitFlowItem(self, ctx:CourseParser.FlowItemContext):
        pass


    # Enter a parse tree produced by CourseParser#type.
    def enterType(self, ctx:CourseParser.TypeContext):
        pass

    # Exit a parse tree produced by CourseParser#type.
    def exitType(self, ctx:CourseParser.TypeContext):
        pass


    # Enter a parse tree produced by CourseParser#ref.
    def enterRef(self, ctx:CourseParser.RefContext):
        pass

    # Exit a parse tree produced by CourseParser#ref.
    def exitRef(self, ctx:CourseParser.RefContext):
        pass


    # Enter a parse tree produced by CourseParser#modes.
    def enterModes(self, ctx:CourseParser.ModesContext):
        pass

    # Exit a parse tree produced by CourseParser#modes.
    def exitModes(self, ctx:CourseParser.ModesContext):
        pass


    # Enter a parse tree produced by CourseParser#object.
    def enterObject(self, ctx:CourseParser.ObjectContext):
        pass

    # Exit a parse tree produced by CourseParser#object.
    def exitObject(self, ctx:CourseParser.ObjectContext):
        pass


    # Enter a parse tree produced by CourseParser#array.
    def enterArray(self, ctx:CourseParser.ArrayContext):
        pass

    # Exit a parse tree produced by CourseParser#array.
    def exitArray(self, ctx:CourseParser.ArrayContext):
        pass


    # Enter a parse tree produced by CourseParser#pair.
    def enterPair(self, ctx:CourseParser.PairContext):
        pass

    # Exit a parse tree produced by CourseParser#pair.
    def exitPair(self, ctx:CourseParser.PairContext):
        pass


    # Enter a parse tree produced by CourseParser#value.
    def enterValue(self, ctx:CourseParser.ValueContext):
        pass

    # Exit a parse tree produced by CourseParser#value.
    def exitValue(self, ctx:CourseParser.ValueContext):
        pass



del CourseParser