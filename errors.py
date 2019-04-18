import sys
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
    global _values_table
    for node in ast.parts:
        if hasattr(node, 'type'):
            if node.type == 'VARIABLE':
                if check_var_declr_type(node.parts[0], node.parts[1], node.parts[2]) == True:
                    _values_table[node.parts[1].parts[0]] = node.parts[0].parts[0].lower()
            elif node.type == 'ASSIGN':
                check_types(node.parts[0], node.parts[1])
            elif node.type == 'RETURN':
                # TODO check if return is situated into a function
                pass
            elif node.type == 'CONTINUE' or node.type == 'BREAK':
                # TODO check if token is situated into loop
                pass
            elif node.type == 'ARRAY':
                # TODO check if array has a negative size
                pass
            elif node.type == 'INDEX':
                # TODO check correctly of index
                # Anton, you should create a function named like check_index() and call it here.
                # You can use is_var_exist function for help
                pass
            else:
                find_semantic_errors(node)


# Return False if an error was found, else return True
def check_var_declr_type(type, id, value = None):
    global _values_table
    if id.parts[0] in _values_table:
        error(1, 'Variable %s is already exist' % id.parts[0])
        return False
    if value is not None:
        if not value.type == 'INT' and not value.type == 'DOUBLE' and not value.type == 'STRING' and not value.type == 'BOOL' and not value.type == 'ID':
            for part in value.parts:
                if check_var_declr_type(type, id, part) == False:
                    return False
        elif value.type == 'ID':
            id_type = is_var_exist(value.parts[0])
            if id_type is None:
                error(1, 'Variable %s is not exist' % value.parts[0])
                return False
            if not type.parts[0] == id_type.lower():
                error(1, 'Variable type "%s" and value type "%s" aren\'t same' % (type.parts[0], id_type.lower()))
                return False
        elif not type.parts[0] == value.type.lower():
            error(1, 'Variable type "%s" and value type "%s" aren\'t same' % (type.parts[0], value.type.lower()))
            return False
    return True


def check_types(var, value):
    var_type = is_var_exist(var)
    if var_type is None:
        error(1, 'Variable %s is not exist' % var)
        return
    if not value.type == 'INT' and not value.type == 'DOUBLE' and not value.type == 'STRING' and not value.type == 'BOOL' and not value.type == 'ID':
        for part in value.parts:
            if not check_types(var, part):
                return False
    elif value.type == 'ID':
        id_type = is_var_exist(value.parts[0])
        if id_type is None:
            error(1, 'Variable %s is not exist' % value.parts[0])
            return False
        if not var_type == id_type.lower():
            error(1, 'Variable type "%s" and value type "%s" aren\'t same' % (var_type, id_type.lower()))
            return False
    elif not var_type == value.type.lower():
        error(1, 'Variable "%s" has a type "%s", but value has a type "%s"' % (var, var_type, value.type.lower()))
        return False

    return True


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