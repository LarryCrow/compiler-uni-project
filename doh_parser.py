import ply.yacc as yacc
from doh_lexer import tokens

# All operations(math or logical) with numbers are defined at the 'expr' rule
# All conditionals are defined at the 'expr' rule too
# The 'stmt' rule is needed for storing statements like some expression or assignment.
# It's expanding
# The 'stmtList' rule is needed for storing expressions that were defined as 'stmt'. It's the main rule at the
# parser for now.

# Precedence is tuple to keep precedence level and associativity of tokens.
# Values are in ascending precedent level. Comma has lower priority, lbrace, rbrace ... have higher priority.


# It's the class for more comfortable AST storing and printing
class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append( str( part ) )
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts


precedence = (
    ('left', 'COMMA'),
    ('right', 'EQUALS'),
    ('nonassoc', 'LOR'),
    ('nonassoc', 'LAND'),
    ('nonassoc', 'EQ', 'NE'),
    ('nonassoc', 'LE', 'GE', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIVIDE', 'INTDIVIDE', 'MODULO'),
    ('right', 'POW'),
    ('right', 'UMINUS', 'LNOT'),
    ('left', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET')
)


# def p_program(p):
#     '''program :
#                | stmtList
#                | program stmtList'''
#     if len(p) == 1:
#         p[0] = ''
#     elif len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = p[1]


# def p_func_declaration(p):
#     '''func_declaration : FUNCTION datatype id LPAREN func_params RPAREN LBRACE stmtList RBRACE'''
#     p[0] = Node('FUNCTION', [p[2], p[3], p[5], p[8]])


def p_stmt_list(p):
    '''stmtList : stmtList stmt
                | stmt'''
    if len(p) == 3:
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('LINE', [p[1]])


def p_stmt(p):
    '''stmt : expr SEMI
            | RETURN expr SEMI
            | assign'''
    if len(p) == 3:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = Node('RETURN', [p[2]])
    else:
        p[0] = p[1]

#
# def p_struct_declaration(p):
#     '''struct_declaration : STRUCT id LBRACE func_params RBRACE'''
#     p[0] = Node('STRUCT', [p[3], p[5]])


def p_func_params(p):
    '''func_params :
                   | func_param
                   | func_params COMMA func_param'''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = Node('PARAMS', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_func_param_declaration(p):
    '''func_param : DATATYPE ID'''
    p[0] = Node(p[1], [p[2]])


def p_assign(p):
    '''assign : ID EQUALS expr SEMI'''
    p[0] = Node('ASSIGN', [p[1], p[3]])


def p_math_expressions(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr MUL expr
            | expr DIVIDE expr
            | expr INTDIVIDE expr
            | expr MODULO expr
            | expr POW expr'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = Node('PLUS', [p[1], p[3]])
        elif p[2] == '-':
            p[0] = Node('MINUS', [p[1], p[3]])
        elif p[2] == '*':
            p[0] = Node('MUL', [p[1], p[3]])
        elif p[2] == '/':
            p[0] = Node('DIV', [p[1], p[3]])
        elif p[2] == '%':
            p[0] = Node('INT DIVIDE', [p[1], p[3]])
        elif p[2] == '%%':
            p[0] = Node('MODULO', [p[1], p[3]])
        elif p[2] == '**':
            p[0] = Node('POW', [p[1], p[3]])


def p_conditionals(p):
    '''expr : expr LE expr
            | expr GE expr
            | expr LT expr
            | expr GT expr
            | expr EQ expr
            | expr NE expr'''
    if p[2] == '<=':
        p[0] = Node('LESS OR EQ', [p[1], p[3]])
    elif p[2] == '>=':
        p[0] = Node('GREATER OR EQ', [p[1], p[3]])
    elif p[2] == '<':
        p[0] = Node('LESS', [p[1], p[3]])
    elif p[2] == '>':
        p[0] = Node('GREATER', [p[1], p[3]])
    elif p[2] == '==':
        p[0] = Node('EQUALS', [p[1], p[3]])
    elif p[2] == '!=':
        p[0] = Node('NOT EQUALS', [p[1], p[3]])


def p_logical_operation(p):
    '''expr : MINUS expr %prec UMINUS
            | expr LAND expr
            | expr LOR expr
            | LNOT expr'''
    if p[1] == '-':
        p[0] = Node('UMINUS', [p[2]])
    elif p[2] == '&&':
        p[0] = Node('AND', [p[1], p[3]])
    elif p[2] == '||':
        p[0] = Node('OR', [p[1], p[3]])
    elif p[1] == '!':
        p[0] = Node('NEGATION', [p[2]])


def p_literals(p):
    '''expr : id
            | INTEGER
            | DOUBLE
            | BOOLEAN
            | STRING
            | LPAREN expr RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_datatype(p):
    '''datatype : DATATYPE'''
    p[0] = Node('TYPE', [p[1]])


def p_id(p):
    '''id : ID'''
    p[0] = Node('ID', [p[1]])


def p_error(p):
    print("Syntax error in input!", p)


# Create parser object
def create_doh_parser():
    return yacc.yacc(debug=1)
