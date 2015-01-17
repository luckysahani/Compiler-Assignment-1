#####################################
# lexer.py
# This file tokenize a java file
# namely  identifier | keyword | separator | operator | literal | comment
#####################################

## List of all tokens

#importing libraries
import ply.lex as lex

tokens = ( 'IDENTIFIER',
           'KEYWORD',
           'SEPERATOR',
           'OPERATOR',
           'LITERAL',
           'COMMENT',
           )


def t_IDENTIFIER(t):
    r'[a-zA-Z$_][a-zA-Z$_0-9]*'
    return t

def t_COMMENT(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(\#.*)'
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
lexer.input('hardik bansal /* hardik */')

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok


