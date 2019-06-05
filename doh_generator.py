from enum import Enum
iter_name = 1
binding = {}
strings = []

class Datatype(Enum):
    int = 'i32'
    double = 'double'
    bool = 'i8'
    string = 'i8*'

# Функция, которая вызывается из main.py
# Возвращает сгенерированный код
def generate_code(ast):
    commands = create_llvm(ast)
    return commands


# Функция, для прохода по первому уровню дерева
# И всяким доп.штукам, который пока не реализованы
def create_llvm(ast):
    code = ''
    funcs = []
    structure = []
    for node in ast.parts:
        if hasattr(node, 'type'):
            if node.type == 'VARIABLE':
                code = code + decl_var_llvm(node)
            if node.type == 'FUNCTION':
                funcs.append(decl_func_llvm(node))
            if node.type == 'STRUCTURE':
                structure.append(decl_struct_llvm(node)) # TODO вот сюда нужно вставить функцию, которая будет возвращать код реализации структуры
                code += decl_struct_llvm(node)
    #res = str(funcs) + code
    return code

def decl_struct_llvm(node):
    global binding
    name = get_llvm_var_name()
    binding[node.parts[0].parts[0]] = name
    fields_types = []
    fields = '{'
    for i in range(len(node.parts[1].parts)):
        fields_types.append(node.parts[1].parts[i].type)
    for j in range(len(fields_types)):
        dtype = Datatype[fields_types[j]].value
        if (j == len(fields_types)-1):
            fields += dtype
        else:
            fields += dtype + ', '
    fields += '}'
    code = f'{name} = type {fields}'
    return code


def decl_func_llvm(node):

    def get_func_params(params):
        return list(map(lambda x: {'type': x.type, 'name': x.parts[0]}, params))

    global binding
    func_type = node.parts[0].parts[0]
    func_name = node.parts[1].parts[0]
    func_params = get_func_params(node.parts[2].parts)
    return ''


def decl_var_llvm(node):
    global binding
    value_type = node.parts[2].type.lower()
    if value_type in ['int', 'string', 'double', 'bool']:
        llvm_name, code = decl_const(node.parts[0].parts[0].lower(), node.parts[2].parts[0])
        binding[node.parts[1].parts[0]] = llvm_name
        return code
    elif value_type == 'id':
        llvm_name, code = decl_var_id(node.parts[0].parts[0].lower(), node.parts[2].parts[0])
        binding[node.parts[1].parts[0]] = llvm_name
        return code
    else:
        llvm_name, code = math_operations(node.parts[0].parts[0].lower(), node.parts[2])
        binding[node.parts[1].parts[0]] = llvm_name
        return code


def decl_const(v_type, value):
    name = get_llvm_var_name()
    if not v_type == 'string':
        llvm_type = Datatype[v_type].value
        alloca = f'{name} = {llvm_alloca(llvm_type)}\n'
        store = f'{llvm_store(llvm_type, str(value), name)}\n'
        code = alloca + store
        return (name, code)
    else:
        return ('', '')


def decl_var_id(v_type, var_name):
    global binding
    llvm_var_load_name = binding[var_name]
    name = get_llvm_var_name()
    load_name = get_llvm_var_name()
    if not v_type == 'string':
        llvm_type = Datatype[v_type].value
        alloca = f'{name} = {llvm_alloca(llvm_type)}\n'
        load = f'{load_name} = {llvm_load(llvm_type, llvm_var_load_name)}\n'
        store = f'{llvm_store(llvm_type, load_name, name)}\n'
        code = alloca + load + store
        return (name, code)
    else:
        return ('', '')


def math_operations(v_type, node):
    l_oper = node.parts[0]
    r_oper = node.parts[1]

    if is_atom(l_oper.type.lower()):
        l_ptr, l_code = decl_const(v_type, l_oper.parts[0])
    elif l_oper.type.lower() == 'id':
        l_ptr, l_code = decl_var_id(v_type, l_oper.parts[0])
    else:
        l_ptr, l_code = math_operations(v_type, l_oper)

    if is_atom(r_oper.type.lower()):
        r_ptr, r_code = decl_const(v_type, r_oper.parts[0])
    elif r_oper.type.lower() == 'id':
        r_ptr, r_code = decl_var_id(v_type, r_oper.parts[0])
    else:
        r_ptr, r_code = math_operations(v_type, r_oper)

    llvm_type = Datatype[v_type].value
    operation = node.type.lower()

    l_var_name = get_llvm_var_name()
    r_var_name = get_llvm_var_name()
    res_name = get_llvm_var_name()
    l_val = f'{l_var_name} = {llvm_load(llvm_type, l_ptr)}\n'
    r_val = f'{r_var_name} = {llvm_load(llvm_type, r_ptr)}\n'
    res_ptr = f'{res_name} = {llvm_alloca(llvm_type)}\n'
    res_name_2 = get_llvm_var_name()
    res = f'{res_name_2} = {llvm_math_action(operation, llvm_type, l_var_name, r_var_name)}\n'
    res_store = f'{llvm_store(llvm_type, res_name_2, res_name)}\n'
    code = l_code + r_code + l_val + r_val + res_ptr + res + res_store
    return (res_name, code) 


def is_atom(type):
    return type in ['int', 'double', 'string', 'bool']


# Math functions


def llvm_math_action(operation, data_type, l_oper, r_oper):
    if operation == 'plus':
        return llvm_plus(data_type, l_oper, r_oper)
    elif operation == 'minus':
        return llvm_minus(data_type, l_oper, r_oper)
    elif operation == 'mul':
        return llvm_mul(data_type, l_oper, r_oper)
    elif operation == 'div':
        return llvm_div(data_type, l_oper, r_oper)
    elif operation == 'pow':
        return llvm_pow(l_oper, r_oper)


def llvm_plus(llvm_type, l_oper, r_oper):
    llvm_oper = 'add' if llvm_type == 'i32' else 'fadd'
    return f'{llvm_oper} {llvm_type} {l_oper}, {r_oper}'


def llvm_minus(llvm_type, l_oper, r_oper):
    llvm_oper = 'sub' if llvm_type == 'i32' else 'fsub'
    return f'{llvm_oper} {llvm_type} {l_oper}, {r_oper}'


def llvm_mul(llvm_type, l_oper, r_oper):
    llvm_oper = 'mul' if llvm_type == 'i32' else 'fmul'
    return f'{llvm_oper} {llvm_type} {l_oper}, {r_oper}'


def llvm_div(llvm_type, l_oper, r_oper):
    llvm_oper = 'sdiv' if llvm_type == 'i32' else 'fdiv'
    return f'{llvm_oper} {llvm_type} {l_oper}, {r_oper}'

def llvm_pow(l_oper, r_oper):
    return f'call double @llvm.powi.f64(double {l_oper}, i32 {r_oper})'


# Some helpful functions to do basic llvm operations
def llvm_load(v_type, ptr):
    return f'load {v_type}, {v_type}* {ptr}'

def llvm_store(v_type, value, ptr):
    return f'store {v_type} {value}, {v_type}* {ptr}'

def llvm_alloca(v_type):
    return f'alloca {v_type}'


# Create variable name for llvm code using global variable 'iter_name'
# return {string} - '%.number'
def get_llvm_var_name():
    global iter_name
    name = f'%.{iter_name}'
    iter_name += 1
    return name