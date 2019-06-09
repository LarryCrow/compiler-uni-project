import ply.yacc as yacc
from errors import error
from models.node import Node
from doh_lexer import tokens

# All operations(math or logical) with numbers are defined at the 'expr' rule
# All conditionals are defined at the 'expr' rule too
# The 'stmt' rule is needed for storing statements like some expression or assignment.
# It's expanding
# The 'stmtList' rule is needed for storing expressions that were defined as 'stmt'. It's the main rule at the
# parser for now.

# Precedence is tuple to keep precedence level and associativity of tokens.
# Values are in ascending precedent level. Comma has lower priority, lbrace, rbrace ... have higher priority.

precedence = (
    ('left', 'COMMA'),
    ('right', 'EQUALS'),
    ('nonassoc', 'LOR'),
    ('nonassoc', 'LAND'),
    ('nonassoc', 'BOR'),
    ('nonassoc', 'BAND'),
    ('nonassoc', 'EQ', 'NE'),
    ('nonassoc', 'LE', 'GE', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIVIDE', 'INTDIVIDE', 'MODULO'),
    ('right', 'POW'),
    ('right', 'UMINUS', 'LNOT'),
    ('left', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'DOT')
)


def p_program(p):
    '''
    program :
            | scope
    '''
    if len(p) == 1:
        p[0] = ''
    elif len(p) == 2:
        p[0] = p[1]


def p_body_block(p):
    'basic_block : LBRACE scope RBRACE'
    p[0] = p[2]


def p_body_block_error(p):
    'basic_block : LBRACE scope error'
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected \'}\'' % p[3].value)


def p_scope(p):
    '''
    scope : scope statement
          | statement
    '''
    if len(p) == 3:
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('SCOPE', [p[1]], 0)


def p_stmt(p):
    '''
    statement : expr SEMI
              | func_declaration
              | struct_definition
              | while
              | goto_mark
              | if-else
              | statement_semi SEMI
    '''
    p[0] = p[1]


def p_stmt_semi_error(p):
    'statement : statement_semi error'
    error(p.lexer.lineno, 'Unexpected symbol "%s". Expected \';\'' % p[2].value)


def p_stmt_semi(p):
    '''
    statement_semi : array
                   | return
                   | goto
                   | loop_keyword
                   | var_declaration
                   | assign
    '''
    p[0] = p[1]


def p_loop(p):
    '''
    while : WHILE expr basic_block
          | DO basic_block WHILE expr SEMI
    '''
    if len(p) == 4:
        p[0] = Node('WHILE', [p[2], p[3]], p.lineno(1))
    else:
        p[0] = Node('DO_WHILE', [p[2], p[4]], p.lineno(5))


def p_loop_error(p):
    '''
    while : WHILE error
          | WHILE expr error
          | DO error
          | DO basic_block error
          | DO basic_block WHILE error
          | DO basic_block WHILE expr error
    '''
    pos = p.lexer.lineno
    if p[1] == 'while':
        if str(p.slice[2]) == 'error':
            error(pos, 'Unexpected symbol \'%s\'. Expected conditional expression' % p[2].value)
        else:
            error(pos, 'Unexpected symbol \'%s\'. Expected \'}\'' % p[3].value)
    else:
        if str(p.slice[2]) == 'error':
            error(pos, 'Unexpected symbol \'%s\'. Expected \'{\'' % p[2].value)
        elif str(p.slice[3]) == 'error':
            error(pos, 'Unexpected symbol \'%s\'. Expected \'while\'' % p[3].value)
        elif str(p.slice[4]) == 'error':
            error(pos, 'Unexpected symbol \'%s\'. Expected conditional expression' % p[4].value)
        else:
            error(pos, 'Unexpected symbol \'%s\'. Expected \';\'' % p[5].value)


def p_loop_keyword(p):
    '''
    loop_keyword : BREAK
                 | CONTINUE
    '''
    p[0] = Node(p[1].upper(), [], p.lineno(1))


def p_if_else(p):
    '''
    if-else : IF expr basic_block
            | IF expr basic_block ELSE basic_block
    '''
    if len(p) == 4:
        p[0] = Node('IF', [p[2], p[3]], p.lineno(1))
    else:
        p[0] = Node('IF_ELSE', [p[2], p[3], p[5]], p.lineno(1))


def p_if_else_error(p):
    '''
    if-else : IF error
            | IF expr error
            | IF expr basic_block ELSE error
    '''
    pos = p.lexer.lineno
    if len(p) == 3:
        error(pos, 'Unexpected symbol \'%s\'. Expected conditional expression' % p[2].value)
    elif len(p) == 4:
        error(pos, 'Unexpected symbol \'%s\'. Expected \'{\'' % p[3].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected \'{\'' % p[5].value)


###### STRUCTURE DEFINITION ######


def p_struct_definition(p):
    'struct_definition : STRUCTURE id struct_body'
    p[0] = Node('STRUCTURE', [p[2], p[3]], p.lineno(1))


def p_struct_declaration_body(p):
    'struct_body : LBRACE struct_fields RBRACE'
    p[0] = p[2]


def p_struct_declarartion_body_error(p):
    '''struct_body : LBRACE struct_fields error
                   | error struct_fields RBRACE'''
    if str(p.slice[1]) == 'error':
        error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected \'{\'' % p[1].value)
    else:
        error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected \',\' or closing bracket' % p[3].value)


def p_struct_fields(p):
    '''
    struct_fields : param
                  | struct_fields COMMA param
    '''
    if len(p) == 2:
        p[0] = Node('FIELDS', [p[1]], p.lineno(1))
    else:
        p[0] = p[1].add_parts([p[3]])


def p_struct_fields_error(p):
    '''
    struct_fields : struct_fields COMMA error
    '''
    pos = p.lexer.lineno
    if len(p) == 3:
        error(pos, 'Unexpected symbol \'%s\'. Expected \',\' or closing bracket' % p[2].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected field' % p[3].value)


###### FUNCTION DECLARATION ######


def p_func_declaration(p):
    'func_declaration : FUNCTION datatype id func_params_paren basic_block'
    p[0] = Node('FUNCTION', [p[2], p[3], p[4], p[5]], p.lineno(1))


def p_func_declaration_str(p):
    'func_declaration : FUNCTION ID id func_params_paren basic_block'
    p[0] = Node('FUNCTION', [Node('TYPE', [p[2]], p.lineno(1)), p[3], p[4], p[5]], p.lineno(1))


def p_func_declaration_error(p):
    '''
    func_declaration : FUNCTION error
                     | FUNCTION datatype error func_params_paren basic_block
                     | FUNCTION datatype id error basic_block
                     | FUNCTION datatype id func_params_paren error
    '''
    pos = p.lexer.lineno
    if str(p.slice[2]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected return type' % p[2].value)
    elif str(p.slice[3]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected function name' % p[3].value)
    elif str(p.slice[4]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected return function params' % p[4].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected \'{\'' % p[5].value)


def p_func_params_paren(p):
    'func_params_paren : LPAREN func_params RPAREN'
    p[0] = p[2]


def p_func_param_paren_error(p):
    'func_params_paren : LPAREN func_params error'
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected \')\'' % p[3].value)


def p_func_params(p):
    '''
    func_params :
                | param
                | func_params COMMA param
    '''
    if len(p) == 1:
        p[0] = Node('PARAMS', [])
    elif len(p) == 2:
        p[0] = Node('PARAMS', [p[1]], p.lineno(1))
    else:
        p[0] = p[1].add_parts([p[3]])


def p_func_params_error(p):
    '''
    func_params : func_params error param
                | func_params COMMA error
    '''
    pos = p.lexer.lineno
    if str(p.slice[2]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected \',\' or closing bracket' % p[2].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected data type' % p[3].value)


def p_param_declaration(p):
    """
    param : ID ID
          | DATATYPE ID
    """
    p[0] = Node(p[1], [p[2]], p.lineno(1))


def p_param_declaration_error(p):
    'param : ID error'
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected variable name' % p[2].value)


def p_func_call(p):
    'expr : id LPAREN args RPAREN'
    p[0] = Node('FUNCTION_CALL', [p[1], p[3]], p.lineno(1))


def p_arguments_braced(p):
    'args_braced : LBRACE args RBRACE'
    p[0] = p[2]


def p_argumantes_braced(p):
    'args_braced : LBRACE args error'
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected \',\' or closing bracket' % p[3].value)


def p_arguments(p):
    '''
    args :
         | expr
         | args COMMA expr
    '''
    if len(p) == 1:
        p[0] = Node('ARGUMENTS', [])
    elif len(p) == 2:
        p[0] = Node('ARGUMENTS', [p[1]], p.lineno(1))
    elif len(p) == 4:
        p[0] = p[1].add_parts([p[3]])


def p_arguments_error(p):
    '''
    args : args COMMA error
    '''
    pos = p.lexer.lineno
    if len(p) == 3:
        error(pos, 'Unexpected symbol \'%s\'. Expected \',\' or closing bracket' % p[2].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected argument' % p[3].value)


def p_var_declaration(p):
    '''
    var_declaration : datatype id EQUALS expr
                    | datatype id
    '''
    if len(p) == 5:
        p[0] = Node('VARIABLE', [p[1], p[2], p[4]], p.lineno(3))
    else:
        p[0] = Node('VARIABLE', [p[1], p[2]], p.lineno(2))


def p_struct_var_declaration(p):
    '''
    var_declaration : ID id
                    | ID id EQUALS args_braced
                    | ID id EQUALS expr
    '''
    if len(p) == 3:
        p[0] = Node('STRUCT_VAR', [Node('TYPE', [p[1]]), p[2]], p.lineno(1))
    elif len(p) == 4 and p[4].type == 'ARGS':
        p[0] = Node('STRUCT_VAR', [Node('TYPE', [p[1]]), p[2], p[4]], p.lineno(1))
    else:
        p[0] = Node('STRUCT_VAR', [Node('TYPE', [p[1]]), p[2], p[4]], p.lineno(1))


def p_var_declaration_error(p):
    '''
    var_declaration : datatype id EQUALS error
                    | ID id EQUALS error
    '''
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected expression' % p[4].value)


###### ASSIGNMENT ######


def p_var_assign(p):
    'assign : id EQUALS expr'
    if len(p) == 4:
        p[0] = Node('ASSIGN', [p[1], p[3]], p.lineno(2))


def p_struct_assign(p):
    '''
    assign : id EQUALS args_braced
           | id DOT ID EQUALS expr
    '''
    if not p[2] == '.':
        p[0] = Node('ASSIGN', [p[1], p[3]], p.lieno(2))
    else:
        p[0] = Node('ASSIGN', [p[1], Node('FIELD', [p[3]]), p[5]], p.lineno(2))


def p_array_assign(p):
    'assign : id LBRACKET expr RBRACKET EQUALS expr'
    p[0] = Node('ASSIGN', [p[1], p[3], p[6]], p.lineno(2))


def p_assign_error(p):
    '''
    assign : id LBRACKET expr RBRACKET EQUALS error
           | id EQUALS error
           | id DOT ID EQUALS error
    '''
    if str(p.slice[3]) == 'error':
        err_val = p[3].value
    elif str(p.slice[5]) == 'error':
        err_val = p[5].value
    else:
        err_val = p[6].value
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected expression' % err_val)


def p_return(p):
    '''
    return : RETURN expr
           | RETURN
    '''
    if len(p) == 3:
        p[0] = Node('RETURN', [p[2]], p.lineno(1))
    else:
        p[0] = Node('RETURN', [], p.lineno(1))


def p_math_expressions(p):
    '''
    expr : expr PLUS expr
         | expr MINUS expr
         | expr MUL expr
         | expr DIVIDE expr
         | expr INTDIVIDE expr
         | expr MODULO expr
         | expr POW expr
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = Node('PLUS', [p[1], p[3]], p.lineno(2))
        elif p[2] == '-':
            p[0] = Node('MINUS', [p[1], p[3]], p.lineno(2))
        elif p[2] == '*':
            p[0] = Node('MUL', [p[1], p[3]], p.lineno(2))
        elif p[2] == '/':
            p[0] = Node('DIV', [p[1], p[3]], p.lineno(2))
        elif p[2] == '%':
            p[0] = Node('INT DIVIDE', [p[1], p[3]], p.lineno(2))
        elif p[2] == '%%':
            p[0] = Node('MODULO', [p[1], p[3]], p.lineno(2))
        elif p[2] == '**':
            p[0] = Node('POW', [p[1], p[3]], p.lineno(2))


def p_conditionals(p):
    '''
    expr : expr LE expr
         | expr GE expr
         | expr LT expr
         | expr GT expr
         | expr EQ expr
         | expr NE expr
    '''
    if p[2] == '<=':
        p[0] = Node('LE', [p[1], p[3]], p.lineno(2))
    elif p[2] == '>=':
        p[0] = Node('GE', [p[1], p[3]], p.lineno(2))
    elif p[2] == '<':
        p[0] = Node('LT', [p[1], p[3]], p.lineno(2))
    elif p[2] == '>':
        p[0] = Node('GT', [p[1], p[3]], p.lineno(2))
    elif p[2] == '==':
        p[0] = Node('EQ', [p[1], p[3]], p.lineno(2))
    elif p[2] == '!=':
        p[0] = Node('NE', [p[1], p[3]], p.lineno(2))


def p_logical_operation(p):
    '''
    expr : MINUS expr %prec UMINUS
         | expr LAND expr
         | expr LOR expr
         | LNOT expr
    '''
    if p[1] == '-':
        p[0] = Node('UMINUS', [p[2]], p.lineno(1))
    elif p[2] == '&&':
        p[0] = Node('LAND', [p[1], p[3]], p.lineno(1))
    elif p[2] == '||':
        p[0] = Node('LOR', [p[1], p[3]], p.lineno(1))
    elif p[1] == '!':
        p[0] = Node('LNOT', [p[2]], p.lineno(1))


def p_bitwise_operation(p):
    '''
    expr : expr BAND expr
         | expr BOR expr
    '''
    if p[2] == '&':
        p[0] = Node('BAND', [p[1], p[3]], p.lineno(1))
    elif p[2] == '|':
        p[0] = Node('BOR', [p[1], p[3]], p.lineno(1))


def p_operation_error(p):
    '''
    expr : expr PLUS error
         | expr MINUS error
         | expr MUL error
         | expr DIVIDE error
         | expr INTDIVIDE error
         | expr MODULO error
         | expr POW error
         | expr LE error
         | expr GE error
         | expr LT error
         | expr GT error
         | expr EQ error
         | expr NE error
         | expr BAND error
         | expr BOR error
         | expr LAND error
         | expr LOR error
    '''
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected expression' % p[3].value)


def p_literals(p):
    '''
    expr : id
         | int
         | double
         | bool
         | str
         | void
         | NULL
         | LPAREN expr RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_parentheses_expr_error(p):
    '''
    expr : LPAREN error
         | LPAREN expr error
    '''
    pos = p.lexer.lineno
    if str(p.slice[2]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected expression' % p[2].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected \')\'' % p[3].value)


def p_const_int(p):
    'int : INTEGER'
    p[0] = Node('INT', [p[1]], p.lineno(1))


def p_const_double(p):
    'double : DOUBLE'
    p[0] = Node('DOUBLE', [p[1]], p.lineno(1))


def p_const_bool(p):
    'bool : BOOL'
    p[0] = Node('BOOL', [p[1]], p.lineno(1))


def p_const_string(p):
    'str : STRING'
    p[0] = Node('STRING', [p[1]], p.lineno(1))


def p_void(p):
    'void : VOID'
    p[0] = Node('VOID', [p[1]], p.lineno(1))


def p_array_init(p):
    '''
    array : datatype id array_size
          | ID id array_size
          | datatype id array_size EQUALS args_braced
          | ID id array_size EQUALS args_braced
    '''
    if len(p) == 4:
        if hasattr(p[1], 'type'):
            p[0] = Node('ARRAY', [p[1], p[2], Node('SIZE', [p[3]])], p.lexer.lineno)
        else:
            p[0] = Node('ARRAY', [Node('TYPE', [p[1]]), p[2], Node('SIZE', [p[3]])], p.lineno(1))
    else:
        if hasattr(p[1], 'type'):
            p[0] = Node('ARRAY', [p[1], p[2], Node('SIZE', [p[3]]), p[5]], p.lexer.lineno)
        else:
            p[0] = Node('ARRAY', [Node('TYPE',[p[1]]), p[2], Node('SIZE', [p[3]]), p[5]], p.lineno(1))


def p_array_size(p):
    'array_size : LBRACKET INTEGER RBRACKET'
    p[0] = p[2]


def p_array_size_error(p):
    '''
    array_size : LBRACKET error
               | LBRACKET INTEGER error
    '''
    pos = p.lexer.lineno
    if str(p.slice[2]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected array index' % p[2].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected \']\'' % p[3].value)


def p_index(p):
    'expr : id LBRACKET expr RBRACKET'
    p[0] = Node('ARRAY_ELEMENT', [p[1], p[3]], p.lineno(1))


def p_index_error(p):
    '''
    expr : id LBRACKET error
         | id LBRACKET expr error
    '''
    pos = p.lexer.lineno
    if str(p.slice[3]) == 'error':
        error(pos, 'Unexpected symbol \'%s\'. Expected array index' % p[3].value)
    else:
        error(pos, 'Unexpected symbol \'%s\'. Expected \']\'' % p[4].value)


def p_struct_field(p):
    'expr : id DOT ID'
    p[0] = Node('STRUCT_FIELD', [p[1], Node('FIELD', [p[3]])], p.lineno(2))


def p_struct_field_error(p):
    'expr : id DOT error'
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected structure field' % p[3].value)


def p_goto(p):
    'goto : GOTO id'
    p[0] = Node('GOTO', [p[2]], p.lineno(1))


def p_goto_error(p):
    'goto : GOTO error'
    error(p.lexer.lineno, 'Unexpected symbol \'%s\'. Expected goto mark' % p[2].value)


def p_goto_mark(p):
    'goto_mark : ID COLON'
    p[0] = Node('GOTO_MARK', [p[1]], p.lineno(1))


def p_datatype(p):
    'datatype : DATATYPE'
    p[0] = Node('TYPE', [p[1]], p.lineno(1))


def p_id(p):
    'id : ID'
    p[0] = Node('ID', [p[1]], p.lineno(1))


def p_error(p):
    if p:
        # error('kl', 'klj')
        pass
    else:
        error("End of file", "Probably there will be ',' or closing bracket")


# Create parser object
def create_doh_parser():
    return yacc.yacc(debug=1)
