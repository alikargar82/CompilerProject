grammar Course;

// ===== ROOT =====
courseFile
    :'{' courseIntroduction COMMA flow '}' EOF
    ;

// ===== COURSE INTRODUCTION =====
courseIntroduction
    : '"course_introduction"' COLON courseIntro
    ;


courseIntro
    : LBRACE
        '"name"' COLON STRING COMMA
        '"author"' COLON STRING COMMA
        '"description"' COLON STRING COMMA
        '"level"' COLON STRING COMMA
        '"tags"' COLON array
      RBRACE
    ;

// ===== FLOW =====
flow
    : '"flow"' COLON arrayOfFlowItems
    ;

arrayOfFlowItems
    : LBRACKET flowItem (COMMA flowItem)* RBRACKET
    ;

flowItem
    : LBRACE
        type
        ((ref?
        modes)
        |
        (modes
        ref)?)
      RBRACE
    ;

type
    :'"type"' COLON TYPES
    ;

ref
    :COMMA '"ref"' COLON STRING
    ;

modes
    :COMMA '"modes"' COLON array
    ;
// ===== JSON STRUCTURE =====
object
    : LBRACE (pair (COMMA pair)*)? RBRACE
    ;

array
    : LBRACKET (value (COMMA value)*)? RBRACKET
    ;

pair
    : STRING COLON value
    ;

value
    : STRING
    | NUMBER
    | BOOLEAN
    | NULL
    | object
    | array
    ;

// ===== TOKENS =====
LBRACE      : '{' ;
RBRACE      : '}' ;
LBRACKET    : '[' ;
RBRACKET    : ']' ;
COMMA       : ',' ;
COLON       : ':' ;
NULL        : 'null' ;

TYPES
    :'"registration"'
    |'"chapter"'
    |'"quiz"'
    |'"exam"'
    |'"resource"'
    ;

STRING
    : '"' (~["\\\r\n] | '\\' .)* '"'
    ;

NUMBER
    : '-'? INT ('.' INT)? (('e'|'E') ('+'|'-')? INT)?
    ;

INT
    : '0' | [1-9] [0-9]*
    ;

BOOLEAN
    : 'true' | 'false'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

LINE_COMMENT 
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;
