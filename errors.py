from contextlib import contextmanager
from models.scope import Scope

_subscribers = []
_num_errors = 0
_values_table = {}
_scopes = []
_cur_scope = None


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
    global _scopes
    global _cur_scope
    if not ast == '':
        _cur_scope = Scope(hash(ast))
        _scopes.append(_cur_scope)
        find_errors(ast)
    else:
        print('File is empty')


def find_errors(ast, inside_func=False, inside_loop=False):
    global _scopes
    global _cur_scope
    for node in ast.parts:
        if hasattr(node, 'type'):
            already_called = False
            if node.type == 'VARIABLE':
                declare_variable(node)
            elif node.type == 'STRUCT_VAR':
                declare_structure_variable(node)
            elif node.type == 'ASSIGN':
                check_assignment(node)
            elif node.type == 'FUNCTION':
                if inside_func:
                    error(node.row_pos, 'Function can\'t be defined inside another function')
                else:
                    f_params = declare_function(node)
                    f_scope = Scope(hash(node), _cur_scope, f_params)
                    _scopes.append(f_scope)
                    _cur_scope = f_scope
                    find_errors(node.parts[3], inside_func=True, inside_loop=inside_loop)
                    already_called = True
                    check_function_returns(node.parts[0].parts[0], node.parts[3])
                    _cur_scope = f_scope.scope
            elif node.type == 'RETURN':
                if not inside_func:
                    error(node.row_pos, 'Return can\'t be used outside function')
            elif node.type == 'FUNCTION_CALL':
                check_function_call(node)
            elif node.type == 'STRUCTURE':
                if inside_func:
                    error(node.row_pos, 'Structure can\'t be declared inside function')
                define_structure(node)
            elif node.type == 'ARRAY':
                declare_array(node)
            elif node.type == 'IF' or node.type == 'IF_ELSE' or node.type == 'WHILE' or node.type == 'DO_WHILE':
                check_conditional_or_loop(node)
                new_scope = Scope(hash(node), _cur_scope, _cur_scope.variables.copy())
                _scopes.append(new_scope)
                _cur_scope = new_scope
                if node.type == 'IF':
                    find_errors(node.parts[1], inside_func=inside_func, inside_loop=inside_loop)
                elif node.type == 'IF_ELSE':
                    find_errors(node.parts[1], inside_func=inside_func, inside_loop=inside_loop)
                    find_errors(node.parts[2], inside_func=inside_func, inside_loop=inside_loop)
                elif node.type == 'WHILE':
                    find_errors(node.parts[1], inside_func=inside_func, inside_loop=True)
                else:
                    find_errors(node.parts[0], inside_func=inside_func, inside_loop=True)
                _cur_scope = new_scope.scope
            elif node.type == 'BREAK' or node.type == 'CONTINUE':
                if not inside_loop:
                    error(node.row_pos, 'Operator \'%s\' can\'t be used outside a loop' % node.type.lower())
            elif node.type == 'GOTO':
                check_goto_call(node)
            elif node.type == 'GOTO_MARK':
                declare_goto_mark(node)


############ DECLARATIONS ############


def declare_variable(variable_node):
    """
    Declare a variable of basic type
    :param: variable_node A Node object with a variable declaration rule
    :return:
    """
    global _cur_scope
    var_type = variable_node.parts[0].parts[0].lower()
    var_name = variable_node.parts[1].parts[0]
    if var_type == 'void':
        error(variable_node.row_pos, 'Variable can\'t have a void type')
        return
    is_var_exist = _cur_scope.is_variable_exist(var_name, True)
    if is_var_exist is not None:
        error(variable_node.row_pos, 'Variable \'%s\' already exists' % var_name)
        return
    if len(variable_node.parts) > 2:
        r_side_type = get_value_type(variable_node.parts[2])
        if var_type == r_side_type or r_side_type == 'null':
            _cur_scope.add_variable(var_name, var_type)
        else:
            error(variable_node.row_pos, 'Value can\'t be assigned to \'%s\' variable' % var_type)
    else:
        _cur_scope.add_variable(var_name, var_type)


def declare_function(function_node):
    """
    Declare a function
    :param function_node: A Node object with a function declaration rule
    :return: List of dictionaries of the form {'name', 'type'} with params or None if function can't be declare
    """
    global _cur_scope
    func_type = function_node.parts[0].parts[0]
    func_name = function_node.parts[1].parts[0]
    is_func_exist = _cur_scope.is_variable_exist(func_name, True)
    if is_func_exist is not None:
        error(function_node.row_pos, 'Function \'%s\' already exists')
        return None
    params = get_function_params(function_node.parts[2])
    _cur_scope.add_variable(func_name, func_type, params)
    return params.copy()


def define_structure(structure_node):
    """
    Declare a structure
    :param structure_node: A Node object with a structure declaration rule
    :return:
    """
    global _cur_scope
    structure_name = structure_node.parts[0].parts[0]
    is_structure_type_exist = _cur_scope.is_variable_exist(structure_name, True)
    if is_structure_type_exist is not None:
        error(structure_node.row_pos, 'Structure \'%s\' is already defined' % structure_name)
    structure_params = get_function_params(structure_node.parts[1])
    import collections
    param_names = list(map(lambda x: x['name'], structure_params))
    param_types = list(map(lambda x: x['type'], structure_params))
    duplicate_params = [name for name, count in collections.Counter(param_names).items() if count > 1]
    if len(duplicate_params) > 0:
        error(structure_node.row_pos, 'There are duplicates of the following params: %s' % duplicate_params)
        return
    is_base_types = all(x in ['int', 'bool', 'double', 'string'] for x in param_types)
    if not is_base_types:
        error(structure_node.row_pos, 'There are fields with non-basic type. '
                                      'All fields should have one of the following type: %s' %
              ['int', 'bool', 'double', 'string'])
        return
    _cur_scope.add_variable(structure_name, 'struct', structure_params)


def declare_array(array_node):
    global _cur_scope
    arr_type = array_node.parts[0].parts[0]
    arr_name = array_node.parts[1].parts[0]
    arr_size = array_node.parts[2].parts[0]
    if _cur_scope.is_variable_exist(arr_name, True) is not None:
        error(array_node.row_pos, 'Array \'%s\' already exists' % arr_name)
        return
    if arr_type.lower() == 'void':
        error(array_node.row_pos, 'Array can\'t have a void type')
        return
    if int(arr_size) == 0:
        error(array_node.row_pos, 'Array size can\'t be equals 0')
        return
    if arr_type.lower() not in ['int', 'string', 'bool', 'double']:
        if _cur_scope.is_variable_exist(arr_type) is None:
            error(array_node.row_pos, 'Type \'%s\' does not exist' % arr_type)
            return
    if len(array_node.parts) == 4:
        arr_values_type = get_function_arguments_types(array_node.parts[3].parts)
        is_same_type = all(x == arr_type for x in arr_values_type)
        if is_same_type:
            _cur_scope.add_variable(arr_name, arr_type, {'size': int(arr_size)})
        else:
            error(array_node.row_pos, 'Not all values have a \'%s\' type' % arr_type)
    else:
        _cur_scope.add_variable(arr_name, arr_type, {'size': int(arr_size)})


def declare_structure_variable(str_var_node):
    """
    Declare structure variable
    :param str_var_node: A Node object with structure variable declaration
    :return:
    """
    global _cur_scope
    var_type = str_var_node.parts[0].parts[0]
    var_name = str_var_node.parts[1].parts[0]
    if _cur_scope.is_variable_exist(var_name, True) is not None:
        error(str_var_node.pow_row, 'Variable \'%s\' already exists' % var_name)
        return
    structure = _cur_scope.is_variable_exist(var_type)
    if structure is None:
        error(str_var_node.row_pos, 'Structure \'%s\' does not exist' % var_type)
        return
    if len(str_var_node.parts) > 2:
        if str_var_node.parts[2].type == 'ARGUMENTS':
            str_args = get_function_arguments_types(str_var_node.parts[2].parts)
            str_params = structure['options']
            if not len(str_args) == len(str_params):
                error(str_var_node.row_pos, 'Numbers of arguments are not the same numbers of structure fields')
                return
            for i in range(0, len(str_args)):
                if not str_args[i] == str_params[i]['type']:
                    error(str_var_node.row_pos, 'Field \'%s\', expected \'%s\' but received \'%s\'' %
                          (str_params[i]['name'], str_params[i]['type'], str_args[i]))
                    return
            _cur_scope.add_variable(var_name, var_type)
        else:
            right_side_type = get_value_type(str_var_node.parts[2])
            if not right_side_type == var_type:
                error(str_var_node.row_pos, 'Value has a \'%s\' type, but needed \'%s\'' % (right_side_type, var_type))
            _cur_scope.add_variable(var_name, var_type)
    else:
        _cur_scope.add_variable(var_name, var_type)


def declare_goto_mark(mark_node):
    global _cur_scope
    mark_name = mark_node.parts[0]
    mark = _cur_scope.is_variable_exist(mark_name)
    if mark is not None:
        error(mark_node.row_pos, 'Variable \'%s\' already exists' % mark_name)
        return
    _cur_scope.add_variable(mark_node.parts[0], 'mark')


######################################


def check_assignment(assignment_node):
    global _cur_scope
    var_name = assignment_node.parts[0].parts[0]
    var = _cur_scope.is_variable_exist(var_name)
    if var is None:
        error(assignment_node.row_pos, 'Variable \'%s\' does not exist' % var_name)
        return
    if var['type'] == 'struct':
        error(assignment_node.row_pos, 'Unexpected symbol \'=\'. Expected a variable name')
    if not hasattr(var, 'type') and var['type'] in ['int', 'double', 'bool', 'string']:
        assign_to_var(var, assignment_node.parts[1])
    elif var['options'] is not None and 'size' in var['options']:
        if not len(assignment_node.parts) == 3:
            error(assignment_node.row_pos, 'It is possible to change only the array element')
            return
        assign_to_array(var, assignment_node.parts[1], assignment_node.parts[2])
    else:
        assign_to_structure(assignment_node)


def assign_to_array(var, index, value):
    index_type = get_value_type(index)
    if not index_type == 'int':
        error(value.row_pos, 'Index must have an \'int\' type')
        return
    value_type = get_value_type(value)
    if not var['type'] == value_type:
        error(value.row_pos, 'Value can\'t be assigned in to \'%s\' variable' % var['type'])


def assign_to_var(var, value):
    value_type = get_value_type(value)
    if not var['type'] == value_type:
        error(value.row_pos, 'Value can\'t be assigned in to \'%s\' variable' % var['type'])


def assign_to_structure(assignment_node):
    global _cur_scope
    var_name = assignment_node.parts[0].parts[0]
    struct = _cur_scope.is_variable_exist(_cur_scope.is_variable_exist(var_name)['type'])
    if len(assignment_node.parts) == 2:
        if assignment_node.parts[1].type == 'ARGUMENTS':
            str_args = get_function_arguments_types(assignment_node.parts[1].parts)
            str_params = struct['options']
            if not len(str_args) == len(str_params):
                error(assignment_node.row_pos, 'Numbers of arguments are not the same numbers of structure fields')
                return
            for i in range(0, len(str_args)):
                if not str_args[i] == str_params[i]['type']:
                    error(assignment_node.row_pos, 'Field \'%s\', expected \'%s\' but received \'%s\'' %
                          (str_params[i]['name'], str_params[i]['type'], str_args[i]))
                    return
        else:
            value_type = get_value_type(assignment_node.parts[1])
            if not struct['name'] == value_type:
                error(assignment_node.row_pos, 'Value can\'t be assigned in to \'%s\' variable' % struct['name'])
    else:
        str_field = assignment_node.parts[1].parts[0]
        if str_field not in list(map(lambda x: x['name'], struct['options'])):
            error(assignment_node.row_pos, 'Field \'%s\' does not exist in \'%s\' structure' %
                  (str_field, struct['name']))
        else:
            str_field_type = get_structure_field_type(str_field, struct)
            right_side_type = get_value_type(assignment_node.parts[2])
            if not str_field_type == right_side_type:
                error(assignment_node.row_pos, 'Value can\'t be assigned in to \'%s\' field' % str_field_type)


def check_function_call(func_node):
    """
    Check function call
    :param func_node: A Node object with function call
    :return:
    """
    global _cur_scope
    func_name = func_node.parts[0].parts[0]
    func_args = func_node.parts[1].parts
    func = _cur_scope.is_variable_exist(func_name)
    if func is None:
        error(func_node.row_pos, 'Function \'%s\' does not exist' % func_name)
        return
    args_types = get_function_arguments_types(func_args)
    func_params = func['options']
    if not len(args_types) == len(func_params):
        error(func_node.row_pos, 'Numbers of arguments are not the same numbers of function parameters')
        return
    if not len(func_params) == 0:
        for i in range(0, len(args_types)):
            if not args_types[i] == func_params[i]['type']:
                error(func_node.row_pos, 'Parameter \'%s\', expected \'%s\' but received \'%s\'' %
                      (func_params[i]['name'], func_params[i]['type'], args_types[i]))
                return
    return func['type']


def check_function_returns(func_type, body_node, func_level=True):
    """
    Check if 'return' exists and it returns the right type
    :param func_type: Type of function
    :param body_node: A Node object with a function body where will be searching
    :param func_level: Flag for designations that it is function scope
    :param returns_list: List with all 'return' and their scopes
    :return:
    """

    for part in body_node.parts:
        if hasattr(part, 'type'):
            if part.type == 'WHILE' or part.type == 'IF':
                check_function_returns(func_type, part.parts[1], False)
            elif part.type == 'DO_WHILE':
                check_function_returns(func_type, part.parts[0], False)
            elif part.type == 'IF_ELSE':
                check_function_returns(func_type, part.parts[1], False)
                check_function_returns(func_type, part.parts[2], False)
            elif part.type == 'RETURN':
                if len(part.parts) > 0:
                    return_type = get_value_type(part.parts[0])
                    if func_type == return_type and not func_type == 'void':
                        return True
                    else:
                        error(part.row_pos,
                              'The return value "%s" is different from what is declared in the function "%s"' % (
                                return_type, func_type))
                        return False
                else:
                    if func_type.lower() == 'void':
                        return True
                    else:
                        error(part.row_pos, 'Function have to return a "%s" value' % func_type)
    if not func_type == 'void' and func_level:
        if func_type == 'int' or func_type == 'double':
            possible_value = '0'
        elif func_type == 'string':
            possible_value = ' '
        else:
            possible_value = 'false'
        print(str(body_node.row_pos) + ':', 'Warning - A function or not all of its branches return a value.'
                                            'If an error occurs, \'%s\' will be returned.' % possible_value)


def check_structure_field(str_node):
    global _cur_scope
    str_var = str_node.parts[0].parts[0]
    str_field = str_node.parts[1].parts[0]
    is_var_exist = _cur_scope.is_variable_exist(str_var)
    if is_var_exist is None:
        error(str_node.row_pos, 'Variable \'%s\' does not exist' % str_var)
        return
    struct_params = _cur_scope.is_variable_exist(is_var_exist['type'])['options']
    for par in struct_params:
        if par['name'] == str_field:
            return par['type']
    error(str_node.row_pos, 'Field \'%s\' does not exist at structure \'%s\'' % (str_field, is_var_exist['type']))


def check_array_element(arr_elem_node):
    global _cur_scope
    arr_var = arr_elem_node.parts[0].parts[0]
    arr_index = arr_elem_node.parts[1]
    array = _cur_scope.is_variable_exist(arr_var)
    if array is None:
        error(arr_elem_node.row_pos, 'Array \'%s\' does not exist' % arr_var)
        return
    if not get_value_type(arr_index) == 'int':
        error(arr_elem_node.row_pos, 'Index should be \'int\' type')
        return
    return array['type']


def check_goto_call(goto_node):
    global _cur_scope
    mark = _cur_scope.is_variable_exist(goto_node.parts[0].parts[0])
    if mark is None or not mark['type'] == 'mark':
        error(goto_node.row_pos, 'Label \'%s\' for \'goto\' operator does not exist' % goto_node.parts[0].parts[0])


def check_conditional_or_loop(node):
    if node.type == 'IF' or node.type == 'IF_ELSE' or node.type == 'WHILE':
        cond_expr = node.parts[0]
    else:
        cond_expr = node.parts[1]
    expr_type = get_value_type(cond_expr)
    if not expr_type == 'bool':
        error(node.row_pos, 'Conditional expression should has a \'bool\' type')


def get_value_type(value_node):
    """
    Gets the node value, calculates the type of this value.
    :param value_node: A Node object with value for calculating
    :return: string with a value type
    """
    if hasattr(value_node, 'type'):
        if is_expression(value_node.type):
            if value_node.type == 'UMINUS':
                return value_node.parts[0].type.lower()
            first = get_value_type(value_node.parts[0])
            if not first:
                return False
            second = get_value_type(value_node.parts[1])
            if not second:
                return False
            compare = is_operation_possible(first, second, value_node.type)
            if not compare['is_possible']:
                error(value_node.row_pos, compare['message'])
                return False
            return compare['message']
        elif value_node.type == 'ID':
            return get_id_type(value_node)
        elif value_node.type == 'FUNCTION_CALL':
            return check_function_call(value_node)
        elif value_node.type == 'ARRAY_ELEMENT':
            return check_array_element(value_node)
        elif value_node.type == 'STRUCT_FIELD':
            return check_structure_field(value_node)
        else:
            return value_node.type.lower()
    elif value_node == 'null':
        return 'null'


def get_id_type(id_node):
    global _cur_scope
    var_id = _cur_scope.is_variable_exist(id_node.parts[0])
    if var_id is None:
        error(id_node.row_pos, 'Variable \'%s\' does not exitst' % id_node.parts[0])
    return var_id['type'] if var_id is not None else None


def get_function_params(params_node):
    """
    Gets a parameters node and return list of dictionaries with name and type these params
    :param params_node: A Node object with params
    :return: List of dictionaries of the form {'name', 'type'} with params
    """
    params = []
    for param in params_node.parts:
        params.append({'name': param.parts[0], 'type': param.type.lower()})
    return params


def get_function_arguments_types(args_list):
    """
    Gets list of arguments of a function and return list of types for this args
    :param args_list: list of string arguments
    :return: list of types
    """
    args = []
    for arg in args_list:
        args.append(get_value_type(arg))
    return args


def get_structure_field_type(field_name, structure):
    for field in structure['options']:
        if field['name'] == field_name:
            return field['type']


def is_expression(val_type):
    """
    Gets a value type and check if it is an expression
    :param val_type: type of some value
    :return: True if value is expression False or not
    """
    not_expression = ['INT', 'DOUBLE', 'STRING', 'BOOL', 'ID', 'FUNCTION_CALL', 'STRUCT_FIELD', 'ARRAY_ELEMENT', 'NULL']
    return val_type not in not_expression


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
        msg = 'int'
    elif a == b:
        is_possible = True
    else:
        msg = "Operation %s can't be used for types '%s' and '%s'" % (type_operation, a, b)

    return {
        'is_possible': is_possible,
        'message': msg
    }


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