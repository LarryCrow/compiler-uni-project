import re as re


# An array of tokens and their definitions that we can uniquely identify
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'while': 'WHILE',
    'do': 'DO',
    'continue': 'CONTINUE',
    'goto': 'GOTO',
    'break': 'BREAK',
    'return': 'RETURN',
    'function': 'FUNCTION',
    'struct': 'STRUCTURE',
    'null': 'NULL'
}

# An array of tokens that need complex regular expressions to define
tokens = [
             # Literals (identifier, integer, double, string, boolean, array)
             'ID', 'INTEGER', 'DOUBLE', 'STRING', 'BOOLEAN', 'ARRAY',

             # Operators
             # +, -, *, **, /, %, %%
             # ||, &&, !
             # <, <=, >, >=, ==, !=)
             'PLUS', 'MINUS', 'POW', 'MUL', 'DIVIDE', 'INTDIVIDE', 'MODULO',
             'LOR', 'LAND', 'LNOT',
             'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

             # Assignment (=)
             'EQUALS',

             # Data type declaration
             'DATATYPE',

             # Delimeters
             # ( )
             # [ ]
             # { }
             # , . ; :
             'LPAREN', 'RPAREN',
             'LBRACKET', 'RBRACKET',
             'LBRACE', 'RBRACE',
             'COMMA', 'PERIOD', 'SEMI', 'COLON',

             # Comments
             'COMMENT',

             # Other
             'NEWLINE', 'ERROR'
         ] + list(reserved.values())

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_POW = r'\*{2}'
t_MUL = r'\*'
t_DIVIDE = r'/'
t_INTDIVIDE = r'%'
t_MODULO = r'%%'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LE = r'<='
t_GE = r'>='
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NE = r'!='
t_EQUALS = r'='

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'

# Identifiers
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    if(re.match(r'(int|string|double|array|boolean)', t.value)):
        t.type = 'DATATYPE'
    elif(re.match(r'(true|false)', t.value)):
        t.type = 'BOOLEAN'
    else:
        t.type = reserved.get(t.value, 'ID')
    return t


# Integer literal
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_DOUBLE = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'


# Comment //
def t_COMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t


# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.value = None
    return t


def t_STRING(t):
    r'(\"|\')([^\\\n]|(\\.))*?(\"|\')'
    t.value = t.value[1:len(t.value) - 1]
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s' at row %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)
