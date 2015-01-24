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

tokens = [ 'WHITESPACE',
           'IDENTIFIER',
           'INTEGER',
           'KEYWORD',
           'SEPERATOR',
           'OPERATOR',
           'LITERAL',
           'COMMENT'] + list(reserved.values()) + list(seperator.values())

ml_comment_regex = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
sl_comment_regex = r'(//.*)'
comment_regex = ml_comment_regex + r'|' + sl_comment_regex
decimal_regex = r'((0)|([1-9][0-9]*)[l|L]?)' + r'|'+ r'([1-9]_+[0-9][0-9_]*[0-9])'
octal_regex = r'0_?([0-7])|([0-7][0-7_]*[0-7])'
hexadecimal_regex = r'(0[xX][0-9abcdefABCDEF][0-9abcdefABCDEF_]*[0-9abcdefABCDEF])'+r'|'+'(0[xX][0-9abcdefABCDEF])'
binary_regex = r''
integer_regex = hexadecimal_regex + r'|' + octal_regex + r'|' + decimal_regex
exp_regex = r'[eE][+-]?[0-9]+'
float_regex = r'[0-9]+' + exp_regex + r'|' + r'[0-9]+\.[0-9]*' + exp_regex + r'|' + '.[0-9]+' + exp_regex
boolean_regex = r'(true)|(false)|(TRUE)|(FALSE)'
char_regex = r'\'.\'' + '|' + r'\'\\[ntvrfa\\\'\"]\''
literal_regex = float_regex + r'|' + boolean_regex + r'|' + char_regex


@TOKEN(literal_regex)
def t_LITERAL(t):
    return t


@TOKEN(decimal_regex)
def t_INTEGER(t):
    return t

def t_WHITESPACE(t):
    r'[ \t\f]'
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
#t_ignore  = ' \t'

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
'''
WHITESPACE,
COMMENT,

''' 
