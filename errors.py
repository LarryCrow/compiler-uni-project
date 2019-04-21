from contextlib import contextmanager

_subscribers = []
_num_errors = 0
_values_table = {}


def error(lineno, message, filename=None):
    '''
    Report a compiler error to all subscribers
    '''
    global _num_errors
    if not filename:
        errmsg = "{}: {}".format(lineno, message)
    else:
        errmsg = "{}:{}: {}".format(filename,lineno,message)
    for subscriber in _subscribers:
        subscriber(errmsg)
    _num_errors += 1


# This is a function to search for semantic errors
# It gets an AST, which is a string, and parses it
# When it finds one of the types where can be error it calls a help-function to process this node
def find_semantic_errors(ast):
    if not ast == '':
        find_errors(ast)
    else:
        print('File is empty')


def find_errors(ast, inside_func=False):
    global _values_table
    for node in ast.parts:
        if hasattr(node, 'type'):
            already_called = False
            if node.type == 'VARIABLE':
                check_var_declaration(node)
            if node.type == 'ASSIGN':
                check_var_assigment(node)
            if node.type == 'FUNCTION':
                if inside_func:
                    error(node.row_pos, 'Function can\'t be defined inside another function')
                else:
                    find_errors(node, True)
                    already_called = True
                    check_function_declaration(node)
            if node.type == 'RETURN':
                if not inside_func:
                    error(node.row_pos, 'Return can\'t be used outside function')
            if node.type == 'FUNCTION CALL':
                check_func_call(node)
            if node.type == 'STRUCTURE':
                if inside_func:
                    error(node.row_pos, 'Structure can\'t be declared inside function')
                check_structure_declaration(node)
            if node.type == 'ARRAY':
                check_array_declaration(node)
            if node.type == 'IF' or node.type == 'IF-ELSE' or node.type == 'WHILE' or node.type == 'DO-WHILE':
                check_conditional_or_loop(node)
            if not already_called:
                find_errors(node, inside_func)


def check_var_declaration(var_node):
    global _values_table
    is_exist = is_var_exist(var_node.parts[1].parts[0])
    if is_exist is not None:
        error(var_node.row_pos, 'Variable "%s" is already exist' % var_node.parts[1].parts[0])
        return
    var_type = var_node.parts[0].parts[0]
    if var_type.lower() == 'void':
        error(var_node.row_pos, 'Variable can\'t has a \'void\' type')
        return
    if is_structure(var_type):
        check_struct_var(var_node)
    else:
        if len(var_node.parts) > 2:
            expr_type = check_type_conformity(var_node.parts[2])
            if not expr_type:
                return
            is_possible = is_operation_possible(var_type, expr_type, 'ASSIGN')
            if is_possible['is_possible']:
                _values_table[var_node.parts[1].parts[0]] = var_type
            else:
                error(var_node.row_pos, "Type '%s' can't be assigned to variable with type '%s'" % (expr_type, var_type))
        else:
            _values_table[var_node.parts[1].parts[0]] = var_type


def check_var_assigment(var_node):
    global _values_table
    is_exist = is_var_exist(var_node.parts[0])
    if is_exist is None:
        error(var_node.row_pos, 'Variable "%s" isn\'t exist' % var_node.parts[1].parts[0])
        return
    var_type = is_exist
    expr_type = check_type_conformity(var_node.parts[1])
    if not expr_type:
        return
    is_possible = is_operation_possible(var_type, expr_type, 'ASSIGN')
    if not is_possible['is_possible']:
        error(var_node.row_pos, "Type '%s' can't be assigned to variable with type '%s'" % (expr_type, var_type))


def check_function_declaration(func_node):
    global _values_table
    is_exist = is_var_exist(func_node.parts[1].parts[0])
    if is_exist is not None:
        error(func_node.row_pos, 'Variable "%s" is already exist' % func_node.parts[1].parts[0])
        return
    func_type = func_node.parts[0].parts[0]
    if has_return(func_type, func_node.parts[3]):
        params = get_params_type(func_node.parts[2])
        _values_table[func_node.parts[1].parts[0]] = {'type' : func_type, 'params': params}


def check_structure_declaration(struct_node):
    global _values_table
    is_exist = is_var_exist(struct_node.parts[1].parts[0])
    if is_exist is not None:
        error(struct_node.row_pos, 'Variable "%s" is already exist' % struct_node.parts[1].parts[0])
        return
    struct_type = struct_node.parts[0].parts[0]
    if len(struct_node.parts[1].parts) > 0:
        fields = get_params_type(struct_node.parts[1])
        _values_table[struct_node.parts[0].parts[0]] = {'type' : struct_type, 'fields': fields}
    else:
        error(struct_node.row_pos, 'The structure has to have fields ')


def check_array_declaration(arr_node):
    global _values_table
    is_here_error = False
    is_exist = is_var_exist(arr_node.parts[1].parts[0])
    if is_exist is not None:
        error(arr_node.row_pos, 'Variable "%s" is already exist' % arr_node.parts[1].parts[0])
        is_here_error = True
    if not arr_node.parts[0].parts[0] == arr_node.parts[2].parts[0]:
        error(arr_node.row_pos, 'Types aren\'t same')
        is_here_error = True
    expr_type = check_type_conformity(arr_node.parts[3])
    if not expr_type or not (expr_type.lower() == 'int' or expr_type.lower() == 'double'):
        error(arr_node.row_pos, 'Illegal type of size value')
        is_here_error = True
    if not is_here_error:
        _values_table[arr_node.parts[1].parts[0]] = arr_node.parts[0].parts[0]


def check_func_call(func_node):
    global _values_table
    is_exist = is_var_exist(func_node.parts[0])
    if is_exist is None:
        error(func_node.row_pos, 'Function %s is not exist' % func_node.parts[0])
        return
    if not len(is_exist['params']) == len(func_node.parts[1].parts):
        error(func_node.row_pos, 'Invalid numbers of variables to function %s' % func_node.parts[0])
        return
    if not check_types_args(func_node.parts[1].parts, is_exist['params']):
        return False


def check_struct_var(struct_var):
    is_struct_exist = is_var_exist(struct_var.parts[0].parts[0])
    if is_struct_exist is None:
        error(struct_var.row_pos, 'Function %s is not exist' % struct_var.parts[0])
        return
    if not len(is_struct_exist['fields']) == len(struct_var.parts[2].parts):
        error(struct_var.row_pos, 'Invalid numbers of variables to function %s' % struct_var.parts[0])
        return
    if not check_types_args(struct_var.parts[2].parts, is_struct_exist['fields']):
        return False
    _values_table[struct_var.parts[1].parts[0]] = struct_var.parts[0].parts[0]


def check_conditional_or_loop(node):
    if node.type == 'IF' or node.type == 'IF-ELSE' or node.type == 'WHILE':
        correct_cond = check_type_conformity(node.parts[0])
        if not correct_cond or not correct_cond == 'bool':
            error(node.row_pos, 'Illegal condition.')
    else:
        correct_cond = check_type_conformity(node.parts[1])
        if not correct_cond or not correct_cond == 'bool':
            error(node.row_pos, 'Illegal condition.')


def check_types_args(args, params):
    """
    Check types of function arguments and function params
    :param args: function arguments
    :param params: function parameters
    :return: True if types are same, else False
    """
    i = 0
    for arg in args:
        if not arg.type.lower() == params[i]:
            error(arg.row_pos, 'Expected "%s" type, but received "%s"' % (params[i], arg.type.lower()))
            return False
        i += 1
    return True


def has_return(func_type, func_node):
    for part in func_node.parts:
        if part.type == 'WHILE' or part.type == 'DO-WHILE' or part.type == 'IF' or part.type == 'IF-ELSE' or part.type == 'STMT_LIST':
            if not has_return(func_type, part):
                return False
        elif part.type == 'RETURN':
            if len(part.parts) > 0:
                return_type = check_type_conformity(part.parts[0])
                if func_type == return_type and not func_type == 'void':
                    return True
                else:
                    error(part.row_pos, 'The return value "%s" is different from what is declared in the function "%s"' % (return_type, func_type))
                    return False
            else:
                if func_type.lower() == 'void':
                    return True
                else:
                    error(part.row_pos, 'Function have to return a "%s" value' % func_type)


def get_params_type(params):
    result = []
    for param in params.parts:
        result.append(param.type)
    return result


def check_type_conformity(expr):
    """
    Check type of all variable in math or logical expression
    :param expression: AST of math or logical expression
    :return: True if all types are equals, False - if they aren't
    """
    if hasattr(expr, 'type'):
        if is_expression(expr):
            first = check_type_conformity(expr.parts[0])
            if not first:
                return False
            second = check_type_conformity(expr.parts[1])
            if not second:
                return False
            compare = is_operation_possible(first, second, expr.type)
            if not compare['is_possible']:
                error(expr.row_pos, compare['message'])
                return False
            return compare['message']
        else:
            return get_data_type(expr)
    elif expr == 'null':
        return 'null'


def get_data_type(a):
    if a.type == 'ID' or a.type == 'FUNCTION CALL':
        id_type = is_var_exist(a.parts[0])
        if id_type is not None:
            return id_type.lower()
        error(a.row_pos, 'Variable "%s" is not exist' % a.parts[0])
        return False
    else:
        return a.type.lower()


def is_expression(expr):
    if (expr.type == 'INT' or expr.type == 'DOUBLE' or expr.type == 'STRING' or
            expr.type == 'BOOL' or expr.type == 'ID' or expr.type == 'FUNCTION CALL'):
        return False
    return True


def is_structure(var_type):
    if var_type == 'INT' or var_type == 'DOUBLE' or var_type == 'STRING' or var_type == 'BOOL':
        return False
    return True


def is_operation_possible(a, b, type_operation):
    """
    Function to check is that operation possible between 2 operands
    :param a: first operand
    :param b: second operand
    :param type_operation: operation for operands
    :return: Dictionary with a shape like {is_possible, message}
             Prop message is needed to show why operation impossible.
    """
    def is_number(val):
        """
        Check if operand is number
        :param val: value for checking
        :return: Bool
        """
        return True if val == 'int' or val == 'double' else False

    def is_logical_operation(op):
        tokens = ['LOR', 'LAND', 'LESS', 'LESS OR EQ', 'GREATER', 'GREATER OR EQ', 'EQUALS', 'NOT EQUALS', 'LNOT']
        return op in tokens

    def is_bitwise_operation(op):
        tokens = ['BOR', 'BAND']
        return op in tokens

    is_possible = False
    msg = ""
    if not a == 'null' and b == 'null' and type_operation == 'ASSIGN':
        is_possible = True
    elif a == 'null' or b == 'null':
        msg = "One of operand '%s' and '%s' is null" % (a, b)
    elif is_logical_operation(type_operation):
        if a == b:
            is_possible = True
            msg = 'bool'
        else:
            msg = 'Can\'t compare values of different types'
        # if type_operation == 'EQ' or type_operation == 'NE':
        #     if a == b:
        #         is_possible = True
        #         msg = 'bool'
        #     else:
        #         msg = 'Can\'t compare values of different types'
        # else:
        #     if a == 'bool' and b == 'bool':
        #         is_possible = True
        #         msg = 'bool'
        #     else:
        #         msg = 'Can\'t compare values of different types'
    elif is_bitwise_operation(type_operation):
        if (a == "bool" or a == "int") and a == b:
            is_possible = True
            msg = a
        else:
            msg = 'Can\'t do bitwise operation "%s" between types "%s" and "%s"' % (type_operation, a, b)
    elif a == 'string' and type_operation == 'PLUS':
        is_possible = True
        msg = 'string'
    elif is_number(a) and is_number(b):
        is_possible = True
        msg = 'double'
    elif a == b:
        is_possible = True
    else:
        msg = "Operation %s can't be used for types '%s' and '%s'" % (type_operation, a, b)

    return {
        'is_possible': is_possible,
        'message': msg
    }


def is_var_exist(var_name):
    '''
    Checking if var is existed. Return it's type if var exists and False if not
    :param var_name: Name of variable which should be checked
    :return: {string} variable's type / {bool} False
    '''
    global _values_table
    return _values_table[var_name] if var_name in _values_table else None


def errors_reported():
    '''
    Return number of errors reported
    '''
    return _num_errors


def clear_errors():
    '''
    Clear the total number of errors reported.
    '''
    global _num_errors
    _num_errors = 0


@contextmanager
def subscribe_errors(handler):
    '''
    Context manager that allows monitoring of compiler error messages.
    Use as follows where handler is a callable taking a single argument
    which is the error message string:
    with subscribe_errors(handler):
         ... do compiler ops ...
    '''
    _subscribers.append(handler)
    try:
        yield
    finally:
        _subscribers.remove(handler)