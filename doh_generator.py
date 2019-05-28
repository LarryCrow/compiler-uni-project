from enum import Enum
command = ''

class Datatype(Enum):
    int = 'i32'
    double = 'double'


# class MathOperations(Enum):
#     '+' = 'add'
#     '-' = 'sub'
#     '*' = 'mul'
#     '/' = 'div'


def generate_code(ast):
    global command
    create_command(ast)
    return command


def create_command(ast):
    for node in ast.parts:
        if hasattr(node, 'type'):
            if node.type == 'VARIABLE':
                var_declaration_generate(node)
            elif node.type == 'ASSIGN':
                assign_generate(node)
            elif node.type == 'PLUS':
                plus_generate()


def var_declaration_generate(node):
    global command
    var_type = node.parts[0].parts[0].lower()
    var_name = node.parts[1].parts[0]
    e_type = Datatype[var_type].value
    command = command + '%t = add ' + str(e_type) + ' %0, %0\n'
    

def assign_generate(node):
    var = node.parts[1]

def plus_generate():
    var = 1