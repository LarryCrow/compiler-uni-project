import ply.lex as lex
import re as re


# An array of tokens that need complex regular expressions to define
tokens = [
             # Literals (identifier, integer, double, string, boolean, array)
             'ID', 'INTEGER', 'DOUBLE', 'STRING', 'BOOLEAN',

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
             'COMMA', 'DOT', 'SEMI', 'COLON',

             # Comments
             'COMMENT', 'NEWLINE',
             # Other
             'ERROR', 'FUNCTION', 'RETURN', 'STRUCTURE', 'DO', 'WHILE', 'BREAK', 'CONTINUE', 'GOTO', 'IF', 'ELSE', 'NULL'
         ]

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
t_DOT = r'\.'
t_SEMI = r';'
t_COLON = r':'

# Identifiers
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    if(re.match(r'(\bint\b|\bstring\b|\bdouble\b|\bboolean\b)', t.value)):
        t.type = 'DATATYPE'
    elif(re.match(r'(\btrue\b|\bfalse\b)', t.value)):
        t.type = 'BOOLEAN'
    elif re.match(r'(\bfunction\b)', t.value):
        t.type = 'FUNCTION'
    elif re.match(r'(\bstruct\b)', t.value):
        t.type = 'STRUCTURE'
    elif re.match(r'(\breturn\b)', t.value):
        t.type = 'RETURN'
    elif re.match(r'(\bdo\b)', t.value):
        t.type = 'DO'
    elif re.match(r'(\bwhile\b)', t.value):
        t.type = 'WHILE'
    elif re.match(r'(\bbreak\b)', t.value):
        t.type = 'BREAK'
    elif re.match(r'(\bcontinue\b)', t.value):
        t.type = 'CONTINUE'
    elif re.match(r'(\bgoto\b)', t.value):
        t.type = 'GOTO'
    elif re.match(r'(\bif\b)', t.value):
        t.type = 'IF'
    elif re.match(r'(\belse\b)', t.value):
        t.type = 'ELSE'
    elif re.match(r'(\bnull\b)', t.value):
        t.type = 'NULL'
    else:
        t.type = 'ID'
    return t


# Floating literal
def t_DOUBLE(t):
    r'[0-9]+.[0-9]+'
    try:
        num = float(t.value)
    except:
        t_error(t)
    if abs(num) > 2^31 - 1:
        t_error(t)
    else:
        return t


# Integer literal
# t_INTEGER = r'[0-9]+'
def t_INTEGER(t):
    r'[0-9]+'
    try:
        num = int(t.value)
    except ValueError:
        t_error(t)
    if abs(num) > 2^31 - 1:
        t_error(t)
    else:
        return t


# Comment //
def t_COMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    t.lexer.start_row_pos = t.lexpos + len(t.value)


# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.value = "Newline"
    t.lexer.start_row_pos = t.lexpos + 1


def t_STRING(t):
    r'(\"|\')([^\\\n]|(\\.))*?(\"|\')'
    t.value = t.value[1:len(t.value) - 1]
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    if re.match(r'(\'|\")', t.value[0]):
      print("Unfinished string at %d, %d" % (t.lineno, t.lexpos - t.lexer.start_row_pos))
    elif re.match(r'(\[|\]|\{|\})', t.value[0]):
      print("Unclosed bracket at %d, %d", (t.lineno, t.lexpos - t.lexer.start_row_pos))
    elif re.match(r'([+|-]?[0-9]+)', t.value):
      print("The number is too large at %d, %d" % (t.lineno, t.lexpos - t.lexer.start_row_pos))
    else:
      print("Illegal character '%s' at %d, %d" % (t.value[0], t.lineno, t.lexpos - t.lexer.start_row_pos))
    t.lexer.skip(1)
