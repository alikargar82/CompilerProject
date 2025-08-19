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
        4,1,26,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,3,0,23,8,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,43,8,2,10,
        2,12,2,46,9,2,1,2,1,2,1,3,1,3,1,3,3,3,53,8,3,1,3,3,3,56,8,3,1,3,
        1,3,3,3,60,8,3,1,3,1,3,3,3,64,8,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,4,
        6,73,8,6,11,6,12,6,74,1,7,1,7,1,7,1,7,3,7,81,8,7,1,7,1,7,1,7,1,7,
        1,7,5,7,88,8,7,10,7,12,7,91,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,0,97,0,20,1,0,0,0,2,27,1,0,0,0,4,38,
        1,0,0,0,6,49,1,0,0,0,8,65,1,0,0,0,10,68,1,0,0,0,12,70,1,0,0,0,14,
        76,1,0,0,0,16,94,1,0,0,0,18,96,1,0,0,0,20,22,3,2,1,0,21,23,3,6,3,
        0,22,21,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,25,3,12,6,0,25,26,
        5,0,0,1,26,1,1,0,0,0,27,28,5,1,0,0,28,29,5,22,0,0,29,30,5,2,0,0,
        30,31,5,22,0,0,31,32,5,3,0,0,32,33,5,22,0,0,33,34,5,4,0,0,34,35,
        5,19,0,0,35,36,5,5,0,0,36,37,3,4,2,0,37,3,1,0,0,0,38,39,5,6,0,0,
        39,44,5,22,0,0,40,41,5,7,0,0,41,43,5,22,0,0,42,40,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,
        47,48,5,8,0,0,48,5,1,0,0,0,49,52,5,9,0,0,50,51,5,10,0,0,51,53,5,
        22,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,56,3,8,4,0,55,
        54,1,0,0,0,55,56,1,0,0,0,56,59,1,0,0,0,57,58,5,11,0,0,58,60,5,22,
        0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,63,1,0,0,0,61,62,5,12,0,0,62,
        64,5,21,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,7,1,0,0,0,65,66,5,13,
        0,0,66,67,3,10,5,0,67,9,1,0,0,0,68,69,5,23,0,0,69,11,1,0,0,0,70,
        72,5,14,0,0,71,73,3,14,7,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,
        0,0,74,75,1,0,0,0,75,13,1,0,0,0,76,77,5,15,0,0,77,80,5,20,0,0,78,
        79,5,16,0,0,79,81,3,16,8,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,
        0,0,82,83,5,17,0,0,83,84,5,6,0,0,84,89,3,18,9,0,85,86,5,7,0,0,86,
        88,3,18,9,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,
        0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,8,0,0,93,15,1,0,0,0,94,95,
        5,22,0,0,95,17,1,0,0,0,96,97,5,18,0,0,97,19,1,0,0,0,9,22,44,52,55,
        59,63,74,80,89
    ]

class CourseParser ( Parser ):

    grammarFileName = "Course.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'name:'", "'author:'", "'description:'", 
                     "'level:'", "'tags:'", "'['", "','", "']'", "'student_data:'", 
                     "'roster_file:'", "'classes_file:'", "'enrollment_mode:'", 
                     "'capacity:'", "'flow:'", "'- type:'", "'ref:'", "'modes:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MODE_NAMES", "LEVEL", "FLOW_TYPE", 
                      "ENROLL_MODE", "STRING", "INT", "BOOLEAN", "WS", "COMMENT" ]

    RULE_courseFile = 0
    RULE_metadata = 1
    RULE_tagList = 2
    RULE_studentData = 3
    RULE_capacity = 4
    RULE_num = 5
    RULE_flow = 6
    RULE_flowItem = 7
    RULE_address = 8
    RULE_mode_type = 9

    ruleNames =  [ "courseFile", "metadata", "tagList", "studentData", "capacity", 
                   "num", "flow", "flowItem", "address", "mode_type" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    MODE_NAMES=18
    LEVEL=19
    FLOW_TYPE=20
    ENROLL_MODE=21
    STRING=22
    INT=23
    BOOLEAN=24
    WS=25
    COMMENT=26

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

        def metadata(self):
            return self.getTypedRuleContext(CourseParser.MetadataContext,0)


        def flow(self):
            return self.getTypedRuleContext(CourseParser.FlowContext,0)


        def EOF(self):
            return self.getToken(CourseParser.EOF, 0)

        def studentData(self):
            return self.getTypedRuleContext(CourseParser.StudentDataContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.metadata()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 21
                self.studentData()


            self.state = 24
            self.flow()
            self.state = 25
            self.match(CourseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.STRING)
            else:
                return self.getToken(CourseParser.STRING, i)

        def LEVEL(self):
            return self.getToken(CourseParser.LEVEL, 0)

        def tagList(self):
            return self.getTypedRuleContext(CourseParser.TagListContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_metadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata" ):
                listener.enterMetadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata" ):
                listener.exitMetadata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetadata" ):
                return visitor.visitMetadata(self)
            else:
                return visitor.visitChildren(self)




    def metadata(self):

        localctx = CourseParser.MetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_metadata)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CourseParser.T__0)
            self.state = 28
            self.match(CourseParser.STRING)
            self.state = 29
            self.match(CourseParser.T__1)
            self.state = 30
            self.match(CourseParser.STRING)
            self.state = 31
            self.match(CourseParser.T__2)
            self.state = 32
            self.match(CourseParser.STRING)
            self.state = 33
            self.match(CourseParser.T__3)
            self.state = 34
            self.match(CourseParser.LEVEL)
            self.state = 35
            self.match(CourseParser.T__4)
            self.state = 36
            self.tagList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.STRING)
            else:
                return self.getToken(CourseParser.STRING, i)

        def getRuleIndex(self):
            return CourseParser.RULE_tagList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagList" ):
                listener.enterTagList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagList" ):
                listener.exitTagList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagList" ):
                return visitor.visitTagList(self)
            else:
                return visitor.visitChildren(self)




    def tagList(self):

        localctx = CourseParser.TagListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tagList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CourseParser.T__5)
            self.state = 39
            self.match(CourseParser.STRING)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 40
                self.match(CourseParser.T__6)
                self.state = 41
                self.match(CourseParser.STRING)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(CourseParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StudentDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CourseParser.STRING)
            else:
                return self.getToken(CourseParser.STRING, i)

        def capacity(self):
            return self.getTypedRuleContext(CourseParser.CapacityContext,0)


        def ENROLL_MODE(self):
            return self.getToken(CourseParser.ENROLL_MODE, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_studentData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStudentData" ):
                listener.enterStudentData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStudentData" ):
                listener.exitStudentData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStudentData" ):
                return visitor.visitStudentData(self)
            else:
                return visitor.visitChildren(self)




    def studentData(self):

        localctx = CourseParser.StudentDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_studentData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CourseParser.T__8)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 50
                self.match(CourseParser.T__9)
                self.state = 51
                self.match(CourseParser.STRING)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 54
                self.capacity()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 57
                self.match(CourseParser.T__10)
                self.state = 58
                self.match(CourseParser.STRING)


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 61
                self.match(CourseParser.T__11)
                self.state = 62
                self.match(CourseParser.ENROLL_MODE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CapacityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(CourseParser.NumContext,0)


        def getRuleIndex(self):
            return CourseParser.RULE_capacity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapacity" ):
                listener.enterCapacity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapacity" ):
                listener.exitCapacity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapacity" ):
                return visitor.visitCapacity(self)
            else:
                return visitor.visitChildren(self)




    def capacity(self):

        localctx = CourseParser.CapacityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_capacity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CourseParser.T__12)
            self.state = 66
            self.num()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CourseParser.INT, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = CourseParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(CourseParser.INT)
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

        def flowItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CourseParser.FlowItemContext)
            else:
                return self.getTypedRuleContext(CourseParser.FlowItemContext,i)


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
        self.enterRule(localctx, 12, self.RULE_flow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(CourseParser.T__13)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.flowItem()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

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

        def FLOW_TYPE(self):
            return self.getToken(CourseParser.FLOW_TYPE, 0)

        def mode_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CourseParser.Mode_typeContext)
            else:
                return self.getTypedRuleContext(CourseParser.Mode_typeContext,i)


        def address(self):
            return self.getTypedRuleContext(CourseParser.AddressContext,0)


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
        self.enterRule(localctx, 14, self.RULE_flowItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CourseParser.T__14)
            self.state = 77
            self.match(CourseParser.FLOW_TYPE)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 78
                self.match(CourseParser.T__15)
                self.state = 79
                self.address()


            self.state = 82
            self.match(CourseParser.T__16)
            self.state = 83
            self.match(CourseParser.T__5)
            self.state = 84
            self.mode_type()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 85
                self.match(CourseParser.T__6)
                self.state = 86
                self.mode_type()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(CourseParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CourseParser.STRING, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_address

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddress" ):
                listener.enterAddress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddress" ):
                listener.exitAddress(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddress" ):
                return visitor.visitAddress(self)
            else:
                return visitor.visitChildren(self)




    def address(self):

        localctx = CourseParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(CourseParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mode_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODE_NAMES(self):
            return self.getToken(CourseParser.MODE_NAMES, 0)

        def getRuleIndex(self):
            return CourseParser.RULE_mode_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMode_type" ):
                listener.enterMode_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMode_type" ):
                listener.exitMode_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMode_type" ):
                return visitor.visitMode_type(self)
            else:
                return visitor.visitChildren(self)




    def mode_type(self):

        localctx = CourseParser.Mode_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mode_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(CourseParser.MODE_NAMES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





