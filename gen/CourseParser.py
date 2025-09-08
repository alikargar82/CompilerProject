# Generated from /home/ali/CompilerProject/Course.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,138,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,1,4,1,4,1,5,1,5,1,5,3,5,
        74,8,5,1,5,1,5,1,5,1,5,3,5,80,8,5,3,5,82,8,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,
        104,8,9,10,9,12,9,107,9,9,3,9,109,8,9,1,9,1,9,1,10,1,10,1,10,1,10,
        5,10,117,8,10,10,10,12,10,120,9,10,3,10,122,8,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,136,8,12,1,12,
        0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,137,0,26,1,0,0,0,2,
        33,1,0,0,0,4,37,1,0,0,0,6,55,1,0,0,0,8,59,1,0,0,0,10,70,1,0,0,0,
        12,85,1,0,0,0,14,89,1,0,0,0,16,94,1,0,0,0,18,99,1,0,0,0,20,112,1,
        0,0,0,22,125,1,0,0,0,24,135,1,0,0,0,26,27,5,10,0,0,27,28,3,2,1,0,
        28,29,5,14,0,0,29,30,3,6,3,0,30,31,5,11,0,0,31,32,5,0,0,1,32,1,1,
        0,0,0,33,34,5,1,0,0,34,35,5,15,0,0,35,36,3,4,2,0,36,3,1,0,0,0,37,
        38,5,10,0,0,38,39,5,2,0,0,39,40,5,15,0,0,40,41,5,18,0,0,41,42,5,
        14,0,0,42,43,5,3,0,0,43,44,5,15,0,0,44,45,5,18,0,0,45,46,5,14,0,
        0,46,47,5,4,0,0,47,48,5,15,0,0,48,49,5,18,0,0,49,50,5,14,0,0,50,
        51,5,5,0,0,51,52,5,15,0,0,52,53,5,18,0,0,53,54,5,11,0,0,54,5,1,0,
        0,0,55,56,5,6,0,0,56,57,5,15,0,0,57,58,3,8,4,0,58,7,1,0,0,0,59,60,
        5,12,0,0,60,65,3,10,5,0,61,62,5,14,0,0,62,64,3,10,5,0,63,61,1,0,
        0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,
        1,0,0,0,68,69,5,13,0,0,69,9,1,0,0,0,70,71,5,10,0,0,71,81,3,12,6,
        0,72,74,3,14,7,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,82,
        3,16,8,0,76,77,3,16,8,0,77,78,3,14,7,0,78,80,1,0,0,0,79,76,1,0,0,
        0,79,80,1,0,0,0,80,82,1,0,0,0,81,73,1,0,0,0,81,79,1,0,0,0,82,83,
        1,0,0,0,83,84,5,11,0,0,84,11,1,0,0,0,85,86,5,7,0,0,86,87,5,15,0,
        0,87,88,5,17,0,0,88,13,1,0,0,0,89,90,5,14,0,0,90,91,5,8,0,0,91,92,
        5,15,0,0,92,93,5,18,0,0,93,15,1,0,0,0,94,95,5,14,0,0,95,96,5,9,0,
        0,96,97,5,15,0,0,97,98,3,20,10,0,98,17,1,0,0,0,99,108,5,10,0,0,100,
        105,3,22,11,0,101,102,5,14,0,0,102,104,3,22,11,0,103,101,1,0,0,0,
        104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,109,1,0,0,0,
        107,105,1,0,0,0,108,100,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,
        110,111,5,11,0,0,111,19,1,0,0,0,112,121,5,12,0,0,113,118,3,24,12,
        0,114,115,5,14,0,0,115,117,3,24,12,0,116,114,1,0,0,0,117,120,1,0,
        0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,122,1,0,0,0,120,118,1,0,
        0,0,121,113,1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,5,13,
        0,0,124,21,1,0,0,0,125,126,5,18,0,0,126,127,5,15,0,0,127,128,3,24,
        12,0,128,23,1,0,0,0,129,136,5,18,0,0,130,136,5,19,0,0,131,136,5,
        21,0,0,132,136,5,16,0,0,133,136,3,18,9,0,134,136,3,20,10,0,135,129,
        1,0,0,0,135,130,1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,135,133,
        1,0,0,0,135,134,1,0,0,0,136,25,1,0,0,0,9,65,73,79,81,105,108,118,
        121,135
    ]

class CourseParser ( Parser ):

    grammarFileName = "Course.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"course_introduction\"'", "'\"name\"'", 
                     "'\"author\"'", "'\"description\"'", "'\"level\"'", 
                     "'\"flow\"'", "'\"type\"'", "'\"ref\"'", "'\"modes\"'", 
                     "'{'", "'}'", "'['", "']'", "','", "':'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "COMMA", "COLON", "NULL", "TYPES", "STRING", 
                      "NUMBER", "INT", "BOOLEAN", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_courseFile = 0
    RULE_courseIntroduction = 1
    RULE_courseIntro = 2
    RULE_flow = 3
    RULE_arrayOfFlowItems = 4
    RULE_flowItem = 5
    RULE_type = 6
    RULE_ref = 7
    RULE_modes = 8
    RULE_object = 9
    RULE_array = 10
    RULE_pair = 11
    RULE_value = 12

    ruleNames =  [ "courseFile", "courseIntroduction", "courseIntro", "flow", 
                   "arrayOfFlowItems", "flowItem", "type", "ref", "modes", 
                   "object", "array", "pair", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    LBRACE=10
    RBRACE=11
    LBRACKET=12
    RBRACKET=13
    COMMA=14
    COLON=15
    NULL=16
    TYPES=17
    STRING=18
    NUMBER=19
    INT=20
    BOOLEAN=21
    WS=22
    LINE_COMMENT=23
    BLOCK_COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CourseFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CourseParser.LBRACE, 0)

        def courseIntroduction(self):
            return self.getTypedRuleContext(CourseParser.CourseIntroductionContext,0)


        def COMMA(self):
            return self.getToken(CourseParser.COMMA, 0)

        def flow(self):
            return self.getTypedRuleContext(CourseParser.FlowContext,0)


        def RBRACE(self):
            return self.getToken(CourseParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(CourseParser.EOF, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_courseFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourseFile" ):
                listener.enterCourseFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourseFile" ):
                listener.exitCourseFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourseFile" ):
                return visitor.visitCourseFile(self)
            else:
                return visitor.visitChildren(self)




    def courseFile(self):

        localctx = CourseParser.CourseFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_courseFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CourseParser.LBRACE)
            self.state = 27
            self.courseIntroduction()
            self.state = 28
            self.match(CourseParser.COMMA)
            self.state = 29
            self.flow()
            self.state = 30
            self.match(CourseParser.RBRACE)
            self.state = 31
            self.match(CourseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CourseIntroductionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CourseParser.COLON, 0)

        def courseIntro(self):
            return self.getTypedRuleContext(CourseParser.CourseIntroContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_courseIntroduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourseIntroduction" ):
                listener.enterCourseIntroduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourseIntroduction" ):
                listener.exitCourseIntroduction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourseIntroduction" ):
                return visitor.visitCourseIntroduction(self)
            else:
                return visitor.visitChildren(self)




    def courseIntroduction(self):

        localctx = CourseParser.CourseIntroductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_courseIntroduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(CourseParser.T__0)
            self.state = 34
            self.match(CourseParser.COLON)
            self.state = 35
            self.courseIntro()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CourseIntroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CourseParser.LBRACE, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.COLON)
            else:
                return self.getToken(CourseParser.COLON, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.STRING)
            else:
                return self.getToken(CourseParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.COMMA)
            else:
                return self.getToken(CourseParser.COMMA, i)

        def RBRACE(self):
            return self.getToken(CourseParser.RBRACE, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_courseIntro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourseIntro" ):
                listener.enterCourseIntro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourseIntro" ):
                listener.exitCourseIntro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourseIntro" ):
                return visitor.visitCourseIntro(self)
            else:
                return visitor.visitChildren(self)




    def courseIntro(self):

        localctx = CourseParser.CourseIntroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_courseIntro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(CourseParser.LBRACE)
            self.state = 38
            self.match(CourseParser.T__1)
            self.state = 39
            self.match(CourseParser.COLON)
            self.state = 40
            self.match(CourseParser.STRING)
            self.state = 41
            self.match(CourseParser.COMMA)
            self.state = 42
            self.match(CourseParser.T__2)
            self.state = 43
            self.match(CourseParser.COLON)
            self.state = 44
            self.match(CourseParser.STRING)
            self.state = 45
            self.match(CourseParser.COMMA)
            self.state = 46
            self.match(CourseParser.T__3)
            self.state = 47
            self.match(CourseParser.COLON)
            self.state = 48
            self.match(CourseParser.STRING)
            self.state = 49
            self.match(CourseParser.COMMA)
            self.state = 50
            self.match(CourseParser.T__4)
            self.state = 51
            self.match(CourseParser.COLON)
            self.state = 52
            self.match(CourseParser.STRING)
            self.state = 53
            self.match(CourseParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CourseParser.COLON, 0)

        def arrayOfFlowItems(self):
            return self.getTypedRuleContext(CourseParser.ArrayOfFlowItemsContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_flow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlow" ):
                listener.enterFlow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlow" ):
                listener.exitFlow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlow" ):
                return visitor.visitFlow(self)
            else:
                return visitor.visitChildren(self)




    def flow(self):

        localctx = CourseParser.FlowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_flow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(CourseParser.T__5)
            self.state = 56
            self.match(CourseParser.COLON)
            self.state = 57
            self.arrayOfFlowItems()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayOfFlowItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(CourseParser.LBRACKET, 0)

        def flowItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CourseParser.FlowItemContext)
            else:
                return self.getTypedRuleContext(CourseParser.FlowItemContext,i)


        def RBRACKET(self):
            return self.getToken(CourseParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.COMMA)
            else:
                return self.getToken(CourseParser.COMMA, i)

        def getRuleIndex(self):
            return CourseParser.RULE_arrayOfFlowItems

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOfFlowItems" ):
                listener.enterArrayOfFlowItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOfFlowItems" ):
                listener.exitArrayOfFlowItems(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayOfFlowItems" ):
                return visitor.visitArrayOfFlowItems(self)
            else:
                return visitor.visitChildren(self)




    def arrayOfFlowItems(self):

        localctx = CourseParser.ArrayOfFlowItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayOfFlowItems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(CourseParser.LBRACKET)
            self.state = 60
            self.flowItem()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 61
                self.match(CourseParser.COMMA)
                self.state = 62
                self.flowItem()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(CourseParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlowItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CourseParser.LBRACE, 0)

        def type_(self):
            return self.getTypedRuleContext(CourseParser.TypeContext,0)


        def RBRACE(self):
            return self.getToken(CourseParser.RBRACE, 0)

        def modes(self):
            return self.getTypedRuleContext(CourseParser.ModesContext,0)


        def ref(self):
            return self.getTypedRuleContext(CourseParser.RefContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_flowItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlowItem" ):
                listener.enterFlowItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlowItem" ):
                listener.exitFlowItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlowItem" ):
                return visitor.visitFlowItem(self)
            else:
                return visitor.visitChildren(self)




    def flowItem(self):

        localctx = CourseParser.FlowItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_flowItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(CourseParser.LBRACE)
            self.state = 71
            self.type_()
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 72
                    self.ref()


                self.state = 75
                self.modes()
                pass

            elif la_ == 2:
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 76
                    self.modes()
                    self.state = 77
                    self.ref()


                pass


            self.state = 83
            self.match(CourseParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CourseParser.COLON, 0)

        def TYPES(self):
            return self.getToken(CourseParser.TYPES, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CourseParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(CourseParser.T__6)
            self.state = 86
            self.match(CourseParser.COLON)
            self.state = 87
            self.match(CourseParser.TYPES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CourseParser.COMMA, 0)

        def COLON(self):
            return self.getToken(CourseParser.COLON, 0)

        def STRING(self):
            return self.getToken(CourseParser.STRING, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef" ):
                listener.enterRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef" ):
                listener.exitRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef" ):
                return visitor.visitRef(self)
            else:
                return visitor.visitChildren(self)




    def ref(self):

        localctx = CourseParser.RefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(CourseParser.COMMA)
            self.state = 90
            self.match(CourseParser.T__7)
            self.state = 91
            self.match(CourseParser.COLON)
            self.state = 92
            self.match(CourseParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(CourseParser.COMMA, 0)

        def COLON(self):
            return self.getToken(CourseParser.COLON, 0)

        def array(self):
            return self.getTypedRuleContext(CourseParser.ArrayContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_modes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModes" ):
                listener.enterModes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModes" ):
                listener.exitModes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModes" ):
                return visitor.visitModes(self)
            else:
                return visitor.visitChildren(self)




    def modes(self):

        localctx = CourseParser.ModesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_modes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(CourseParser.COMMA)
            self.state = 95
            self.match(CourseParser.T__8)
            self.state = 96
            self.match(CourseParser.COLON)
            self.state = 97
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CourseParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CourseParser.RBRACE, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CourseParser.PairContext)
            else:
                return self.getTypedRuleContext(CourseParser.PairContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.COMMA)
            else:
                return self.getToken(CourseParser.COMMA, i)

        def getRuleIndex(self):
            return CourseParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = CourseParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CourseParser.LBRACE)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 100
                self.pair()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 101
                    self.match(CourseParser.COMMA)
                    self.state = 102
                    self.pair()
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 110
            self.match(CourseParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(CourseParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(CourseParser.RBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CourseParser.ValueContext)
            else:
                return self.getTypedRuleContext(CourseParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.COMMA)
            else:
                return self.getToken(CourseParser.COMMA, i)

        def getRuleIndex(self):
            return CourseParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CourseParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(CourseParser.LBRACKET)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2954240) != 0):
                self.state = 113
                self.value()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 114
                    self.match(CourseParser.COMMA)
                    self.state = 115
                    self.value()
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 123
            self.match(CourseParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CourseParser.STRING, 0)

        def COLON(self):
            return self.getToken(CourseParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(CourseParser.ValueContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = CourseParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CourseParser.STRING)
            self.state = 126
            self.match(CourseParser.COLON)
            self.state = 127
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CourseParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(CourseParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(CourseParser.BOOLEAN, 0)

        def NULL(self):
            return self.getToken(CourseParser.NULL, 0)

        def object_(self):
            return self.getTypedRuleContext(CourseParser.ObjectContext,0)


        def array(self):
            return self.getTypedRuleContext(CourseParser.ArrayContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CourseParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(CourseParser.STRING)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(CourseParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(CourseParser.BOOLEAN)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(CourseParser.NULL)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.object_()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





