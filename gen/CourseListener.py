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