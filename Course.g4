grammar Course;

// ===== ROOT =====
courseFile
    : metadata studentData? flow EOF
    ;

// ===== METADATA =====
metadata
    : 'name:' STRING
      'author:' STRING
      'description:' STRING
      'level:' LEVEL
      'tags:' tagList
    ;

tagList
    : '[' STRING (',' STRING)* ']'
    ;


// ===== STUDENT DATA =====
studentData
    : 'student_data:'
      ('roster_file:' STRING)?
      ('capacity:' INT)?
      ('classes_file:' STRING)?
      ('enrollment_mode:' ENROLL_MODE)?
    ;

// ===== FLOW =====
flow
    : 'flow:'  flowItem+
    ;

flowItem
    : '- type:' FLOW_TYPE
      ('ref:'  STRING )?
      'modes:' '[' mode_type (',' mode_type)* ']'
    ;

mode_type
    : MODE_NAMES ;

// ===== TYPES =====

MODE_NAMES
    :'form' | 'audio' | 'url' | 'video' | 'text' | 'mcq' | 'tf' | 'coding' | 'essay' | 'short_answer'
    ;

LEVEL
    : 'beginner' | 'intermediate' | 'advanced'
    ;

FLOW_TYPE
    : 'registration' | 'chapter' | 'quiz' | 'exam' | 'resource'
    ;

ENROLL_MODE
    : 'open' | 'invite' | 'restricted'
    ;

STRING
    :  '"' (~["\r\n])* '"'
    ;


INT
    : [0-9]+
    ;

BOOLEAN
    : 'true' | 'false'
    ;

// ===== INDENTATION  =====


WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT : '#' ~[\r\n]* -> skip ;