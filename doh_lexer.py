import ply.lex as lex
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
             'ERROR', 'FUNCTION', 'RETURN', 'STRUCTURE'
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
t_RETURN = r'return'

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
    if(re.match(r'(\bint\b|\bstring\b|\bdouble\b|\barray\b|\bboolean\b)', t.value)):
        t.type = 'DATATYPE'
    elif(re.match(r'(\btrue\b|\bfalse\b)', t.value)):
        t.type = 'BOOLEAN'
    elif re.match(r'(\bfunction\b)', t.value):
        t.type = 'FUNCTION'
    elif re.match(r'(\bstruct\b)', t.value):
        t.type = 'STRUCTURE'
    elif re.match(r'(\breturn\b)', t.value):
        t.type = 'RETURN'
    else:
        t.type = reserved.get(t.value, 'ID')
    return t


# Integer literal
# t_INTEGER = r'[0-9]+'
def t_INTEGER(t):
  r'[0-9]+'
  try:
    num = int(t.value)
  except:
    t_error(t)
  if abs(num) > 2^31 - 1:
    t_error(t)
  else:
    return t

# Floating literal
t_DOUBLE = r'[0-9]+.[0-9]+'


# Comment //
def t_COMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    t.lexer.pos_in_line = t.lexpos + len(t.value)
    return t


# Define a rule so we can track line numbers
# def t_NEWLINE(t):
#     r'\n'
#     t.lexer.lineno += len(t.value)
#     t.value = "Newline"
#     t.lexer.pos_in_line = t.lexpos + 1
#     return t


def t_STRING(t):
    r'(\"|\')([^\\\n]|(\\.))*?(\"|\')'
    t.value = t.value[1:len(t.value) - 1]
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\n'


# Error handling rule
def t_error(t):
    print("\n")
    if re.match(r'(\'|\")', t.value[0]):
      print("Unfinished string at row %d, %d" % (t.lineno, t.lexpos - t.lexer.pos_in_line))
    elif re.match(r'(\[|\]|\{|\})', t.value[0]):
      print("Unclosed bracket at row %d, %d", (t.lineno, t.lexpos - t.lexer.pos_in_line))
    elif re.match(r'([+|-]?[0-9]+)', t.value):
      print("The number is too large at row %d, %d", (t.lineno, t.lexpos - t.lexer.pos_in_line))
    else:
      print("Illegal character '%s' at row %d, %d" % (t.value[0], t.lineno, t.lexpos - t.lexer.pos_in_line))
    t.lexer.skip(1)
    print("\n")
