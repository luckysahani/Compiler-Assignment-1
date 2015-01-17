#####################################
# lexer.py
# This file tokenize a java file
# namely  identifier | keyword | separator | operator | literal | comment
#####################################

## List of all tokens

#importing libraries
import ply.lex as lex
import sys

reserved = {
  'abstract' : 'ABSTRACT' ,
  'continue' : 'CONTINUE' , 
  'goto'  : 'GOTO' ,
  'package' : 'PACKAGE' ,
  'switch'  : 'SWITCH' ,
  'assert'  : 'ASSERT' ,
  'default' : 'DEFAULT' ,
  'if'  : 'IF' ,
  'private' : 'PRIVATE' ,
  'this'  : 'THIS' ,
  'boolean' : 'BOOLEAN' ,
  'do'  : 'DO' ,
  'implements'  : 'IMPLEMENTS' ,
  'protected' : 'PROTECTED' ,
  'throw' : 'THROW' ,
  'break' : 'BREAK' ,
  'double' : 'DOUBLE' ,
  'import'  : 'IMPORT' ,
  'public'  : 'PUBLIC' ,
  'throws': 'THROWS' ,
  'byte'  : 'BYTE' ,
  'else'  : 'ELSE' ,
  'instanceof'  : 'INSTANCEOF' ,
  'return'  : 'RETURN' ,
  'transient' : 'TRANSIENT' ,
  'case'  : 'CASE' ,
  'extends' : 'EXTENDS' ,
  'int' : 'INT' ,
  'short' : 'SHORT' ,
  'try' : 'TRY' ,
  'catch' : 'CATCH' ,
  'final' : 'FINAL' ,
  'interface' : 'INTERFACE' ,
  'static'  : 'STATIC' ,
  'void'  : 'VOID' ,
  'char'  : 'CHAR' ,
  'finally' : 'FINALLY' ,
  'long'  : 'LONG' ,
  'strictfp'  :  'STRCITFP' ,
  'volatile'  : 'VOLATILE' ,
  'class' : 'CLASS' ,
  'float' : 'FLOAT' ,
  'native' : 'NATIVE' ,
  'super' : 'SUPER' ,
  'while' : 'WHILE' ,
  'const' : 'CONST' ,
  'for' : 'FOR' ,
  'new' : 'NEW' , 
  'synchronized' : 'SYNCHRONIZED'
}
seperator = {
  ';' : 'SEMICOLON',
  ',' : 'COMMA' ,
  '.' : 'DOT' ,
  '(' : 'LROUNPAREN' ,
  ')' : 'RROUNPAREN' ,
  '{' : 'LCURPAREN' ,
  '}' : 'RCURPAREN' ,
  '[' : 'LSQPAREN' ,
  ']' : 'RSQPAREN' 
}

tokens = ['IDENTIFIER',
           'KEYWORD',
           'SEPERATOR',
           'OPERATOR',
           'LITERAL',
           'COMMENT'] + list(reserved.values()) + list(seperator.values())

def t_IDENTIFIER(t):
    r'[a-zA-Z$_][a-zA-Z$_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

def t_SEPERATOR(t):
    r'[;,\.\(\)\{\}\[\]]'
    t.type = seperator.get(t.value,'SEPERATOR')   # Check for seperators
    return t
def t_COMMENT(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(\#.*)'
    return t
    # No return value. Token discarded

def t_OPERATOR(t):
    r'(\=)|(\>)|(\<)|(\!)|(\~)|(\?)|(\:)|(\=\=)|(\<\=)|(\>\=)|(\!\=)|(\&\&)|(\|\|)|(\+\+)|(\-\-)|(\+)|(\-)|(\*)|(\/)|(\&)|(\|)|(\^)|(\%)|(\<\<)|(\>\>)|(\>\>\>)|(\+\=)|(\-\=)|(\*\=)|(\/\=)|(\&\=)|(\|\=)|(\^\=)|(\%\=)|(\<\<\=)|(\>\>\=)|(\>\>\=)'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1) 

# Build the lexer
lexer = lex.lex()

lexer.input((open(sys.argv[1],'r')).read())

while True:
    tok = lexer.token()
    if not tok: break      
    print tok


