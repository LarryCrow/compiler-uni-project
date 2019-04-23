from doh_lexer import *
from doh_parser import *
import sys
import argparse


def create_params_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-parameters')

    return parser


pr = create_params_parser()
namespace = pr.parse_args(sys.argv[1:])
lexer = lex.lex()
with open('sample.doh', 'r', encoding="UTF-8") as r:
    data = r.read()
    lexer.start_row_pos = 0
    lexer.input(data)
    import sys
    from errors import subscribe_errors, find_semantic_errors, errors_reported
    parser = create_doh_parser()
    with subscribe_errors(lambda msg: sys.stdout.write(msg+"\n")):
        program = parser.parse()
        if errors_reported() == 0:
            #find_semantic_errors(program)
            if errors_reported() == 0:
                with open('result.txt', 'w') as w:
                    w.write(str(program))
