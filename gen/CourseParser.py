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
        4,1,14,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,3,1,23,8,1,1,1,1,1,1,2,
        1,2,1,2,1,2,5,2,31,8,2,10,2,12,2,34,9,2,3,2,36,8,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,1,4,0,0,5,0,2,4,6,8,
        0,0,55,0,10,1,0,0,0,2,13,1,0,0,0,4,26,1,0,0,0,6,39,1,0,0,0,8,49,
        1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,22,5,1,0,0,14,
        19,3,6,3,0,15,16,5,5,0,0,16,18,3,6,3,0,17,15,1,0,0,0,18,21,1,0,0,
        0,19,17,1,0,0,0,19,20,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,22,14,
        1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,25,5,2,0,0,25,3,1,0,0,0,26,
        35,5,3,0,0,27,32,3,8,4,0,28,29,5,5,0,0,29,31,3,8,4,0,30,28,1,0,0,
        0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,36,1,0,0,0,34,32,
        1,0,0,0,35,27,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,4,0,0,
        38,5,1,0,0,0,39,40,5,8,0,0,40,41,5,6,0,0,41,42,3,8,4,0,42,7,1,0,
        0,0,43,50,5,8,0,0,44,50,5,9,0,0,45,50,5,11,0,0,46,50,5,7,0,0,47,
        50,3,2,1,0,48,50,3,4,2,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,
        0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,9,1,0,0,0,5,19,22,
        32,35,49
    ]

class CourseParser ( Parser ):

    grammarFileName = "Course.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "']'", "','", "':'", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                      "COMMA", "COLON", "NULL", "STRING", "NUMBER", "INT", 
                      "BOOLEAN", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_courseFile = 0
    RULE_object = 1
    RULE_array = 2
    RULE_pair = 3
    RULE_value = 4

    ruleNames =  [ "courseFile", "object", "array", "pair", "value" ]

    EOF = Token.EOF
    LBRACE=1
    RBRACE=2
    LBRACKET=3
    RBRACKET=4
    COMMA=5
    COLON=6
    NULL=7
    STRING=8
    NUMBER=9
    INT=10
    BOOLEAN=11
    WS=12
    LINE_COMMENT=13
    BLOCK_COMMENT=14

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

        def object_(self):
            return self.getTypedRuleContext(CourseParser.ObjectContext,0)


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
            self.state = 10
            self.object_()
            self.state = 11
            self.match(CourseParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(CourseParser.LBRACE)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 14
                self.pair()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 15
                    self.match(CourseParser.COMMA)
                    self.state = 16
                    self.pair()
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 24
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
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CourseParser.LBRACKET)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2954) != 0):
                self.state = 27
                self.value()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 28
                    self.match(CourseParser.COMMA)
                    self.state = 29
                    self.value()
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 37
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
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CourseParser.STRING)
            self.state = 40
            self.match(CourseParser.COLON)
            self.state = 41
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
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(CourseParser.STRING)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(CourseParser.NUMBER)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(CourseParser.BOOLEAN)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(CourseParser.NULL)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.object_()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
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





