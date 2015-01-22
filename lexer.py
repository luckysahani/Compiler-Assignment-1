#####################################
# lexer.py
# This file tokenize a java file
# namely  identifier | keyword | separator | operator | literal | comment
#####################################

## List of all tokens

#importing libraries
import ply.lex as lex
from ply.lex import TOKEN
import sys

#definations of different regex

ml_comment_regex = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
sl_comment_regex = r'(//.*)'
comment_regex = ml_comment_regex + r'|' + sl_comment_regex
decimal_regex = r'(0)|[1-9][0-9]*'
octal_regex = r'0[1-9][0-9]*'
hexadecimal = r'0[xX][1-9][0-9]*'
integer_regex = hexadecimal + r'|' + octal_regex + r'|' + decimal_regex
exp_regex = r'[eE][+-]?[0-9]+'
float_regex = r'[0-9]+' + exp_regex + '|' + r'[0-9]+\.[0-9]*' + exp_regex + '|' + '.[0-9]+' + exp_regex
boolean_regex = r'(true)|(false)|(TRUE)|(FALSE)'
char_regex = r'\'.\'' + '|' + r'\'\\[ntvrfa\\\'\"]\''
literal_regex = float_regex + r'|' + integer_regex + r'|' + boolean_regex + r'|' + char_regex


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


@TOKEN(literal_regex)
def t_LITERAL(t):
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z$_][a-zA-Z$_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

@TOKEN(comment_regex)
def t_COMMENT(t):
    return t
    # No return value. Token discarded

def t_SEPERATOR(t):
    r'[;,\.\(\)\{\}\[\]]'
    t.type = seperator.get(t.value,'SEPERATOR')   # Check for seperators
    return t

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

# Give the lexer some input
#lexer.input("hardik bansal TRUE 0x123  1.00E-05 '.'/* hardik */")

# Tokenize
lexer.input((open('sample.java','r')).read())

while True:
    tok = lexer.token()
    if not tok: break      
    print tok
