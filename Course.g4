grammar Course;

// ===== ROOT =====
courseFile
    : object EOF
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
