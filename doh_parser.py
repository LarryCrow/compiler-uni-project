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
        if self.type == '':
            return self.parts_str().replace("\n", "\n")
        else:
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


def p_program(p):
    '''program :
               | basic_block'''
    if len(p) == 1:
        p[0] = ''
    elif len(p) == 2:
        p[0] = Node('PROGRAM', [p[1]])


def p_basic_block(p):
    '''basic_block : stmt_list'''
    p[0] = p[1]


def p_func_declaration(p):
    '''func_declaration : FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACE'''
    p[0] = Node('FUNCTION', [p[2], p[3], p[5], p[8]])


# def p_func_declaration_error(p):
#     '''func_declaration : FUNCTION error RBRACE'''
#     print('Syntax error in function declaration in a row %d' % p.lineno(2))


def p_stmt_list(p):
    '''stmt_list : stmt_list statement
                 | statement'''
    if len(p) == 3:
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('', [p[1]])


def p_stmt(p):
    '''
    statement : expr SEMI
              | var_declaration
              | return
              | assign
              | func_declaration
              | struct_declaration
              | while
              | BREAK SEMI
              | CONTINUE SEMI
              | GOTO ID SEMI
              | goto_mark
              | if-else
    '''
    if p[1] == 'break':
        p[0] = Node('BREAK', [])
    elif p[1] == 'continue':
        p[0] = Node('CONTINUE', [])
    elif p[1] == 'goto':
        p[0] = Node('GOTO', [p[2]])
    else:
        p[0] = p[1]


def p_loops(p):
    '''
    while : WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE
          | DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI
    '''
    if len(p) == 8:
        p[0] = Node('WHILE', [p[3], p[6]])
    else:
        p[0] = Node('DO-WHILE', [p[3], p[7]])


def p_if_else(p):
    '''
    if-else : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE
            | IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE
    '''
    if len(p) == 7:
        p[0] = Node('IF', [p[3], p[6]])
    else:
        p[0] = Node('IF-ELSE', [p[3], p[6], p[10]])


def p_struct_declaration(p):
    '''
    struct_declaration : STRUCTURE id LBRACE params RBRACE
    '''
    p[0] = Node('STRUCTURE', [p[2], p[4]])


def p_struct_field(p):
    '''
    expr : ID DOT ID
    '''
    p[0] = Node('STRUCT-FIELD', [p[1], p[3]])


# def p_struct_declaration_error(p):
#     '''struct_declaration : STRUCTURE error RBRACE'''
#     print('Syntax error in structure declaration in a row %d' % p.lineno(2))


def p_params(p):
    '''params :
              | param
              | params COMMA param'''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = Node('PARAMS', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


# def p_params_error(p):
#     '''params : param error
#               | params COMMA error param'''
#     if len(p) == 2:
#         print('Syntax error in parameters in a row %d' % p[1].lineno)
#     elif len(p) == 3:
#         print('Syntax error in parameters in a row %d' % p[2].lineno)
#     else:
#         print('Syntax error in parameters in a row %d' % p[3].lineno)


def p_param_declaration(p):
    '''param : DATATYPE ID'''
    p[0] = Node(p[1], [p[2]])


# def p_param_declaration_error(p):
#     '''param : DATATYPE ID error'''
#     print('Syntax error in a parameter declaration in a row $d' % p[3].lineno)


def p_func_call(p):
    '''expr : ID LPAREN args RPAREN'''
    p[0] = Node('FUNCTION CALL', [p[1], p[3]])


def p_arguments(p):
    '''args :
            | expr
            | args COMMA expr'''
    if len(p) == 1:
        pass
    elif len(p) == 2:
        p[0] = Node('ARGUMENTS', [p[1]])
    elif len(p) == 4:
        p[0] = p[1].add_parts([p[3]])


# def p_arguments_error(p):
#     '''args : error'''
#     print('Syntax error in a function arguments in a row %d' % p.slice[1].lineno)


def p_var_declaration(p):
    '''
    var_declaration : datatype id EQUALS expr SEMI
    '''
    p[0] = Node('VARIABLE', [p[1], p[2], p[4]])


def p_assign(p):
    '''assign : ID EQUALS expr SEMI'''
    p[0] = Node('ASSIGN', [p[1], p[3]])


def p_return(p):
    '''
    return : RETURN expr SEMI
           | RETURN SEMI
    '''
    if len(p) == 4:
        p[0] = Node('RETURN', [p[2]])
    else:
        p[0] = Node('RETURN', [])


# def p_assign_error(p):
#     '''assign : EQUALS error SEMI'''
#     print('Syntax error in an assignment operation in a row %d' % p.slice[2].lineno)


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
            | NULL
            | LPAREN expr RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_array_init(p):
    '''
    expr : datatype LBRACKET expr RBRACKET
    '''
    p[0] = Node('ARRAY', [p[1], 'SIZE:\n\t' + str(p[3])])


def p_index(p):
    '''
    expr : ID LBRACKET expr RBRACKET
    '''
    p[0] = Node('INDEX', [p[1], p[3]])


def p_goto_mark(p):
    '''goto_mark : ID COLON'''
    p[0] = Node('GOTO-MARK', [p[1]])


def p_datatype(p):
    '''datatype : DATATYPE'''
    p[0] = Node('TYPE', [p[1]])


def p_id(p):
    '''id : ID'''
    p[0] = Node('ID', [p[1]])


def p_error(p):
    if p:
        print("Syntax error in input at token '%s' at %d, %d" % (p.value, p.lineno, p.lexpos - p.lexer.start_row_pos))
    else:
        print("End of file", "Syntax error. No more input.")


# Create parser object
def create_doh_parser():
    return yacc.yacc(debug=1)
