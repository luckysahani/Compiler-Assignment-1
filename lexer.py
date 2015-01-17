#####################################
# lexer.py
# This file tokenize a java file
# namely  identifier | keyword | separator | operator | literal | comment
#####################################

## List of all tokens

#importing libraries
import ply.lex as lex
from ply.lex import TOKEN

tokens = ( 'LITERAL',
           'IDENTIFIER',
           'KEYWORD',
           'SEPERATOR',
           'OPERATOR',
           'COMMENT',
           )

#definations of different regex

ml_comment_regex = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
sl_comment_regex = r'(\#.*)'
comment_regex = ml_comment_regex + r'|' + sl_comment_regex
decimal_regex = r'(0)|[1-9][0-9]*'
octal_regex = r'0[1-9][0-9]*'
hexadecimal = r'0[xX][1-9][0-9]*'
integer_regex = hexadecimal + r'|' + octal_regex + r'|' + decimal_regex
exp_regex = r'[eE][+-]?[0-9]+'
float_regex = r'[0-9]+' + exp_regex + '|' + r'[0-9]+\.[0-9]*' + exp_regex + '|' + '.[0-9]+' + exp_regex
boolean_regex = r'(true)|(false)|(TRUE)|(FALSE)'
char_regex = r'\'[.]\''
literal_regex = float_regex + r'|' + integer_regex + r'|' + boolean_regex + r'|' + char_regex

@TOKEN(literal_regex)
def t_LITERAL(t):
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z$_][a-zA-Z$_0-9]*'
    return t

@TOKEN(comment_regex)
def t_COMMENT(t):
    return t
    # No return value. Token discarded

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input("hardik bansal TRUE 0x123  1.00E-05 '.'/* hardik */")

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok


