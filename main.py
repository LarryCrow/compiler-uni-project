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
parser = create_doh_parser()
with open('sample.doh', 'r', encoding="UTF-8") as r:
    data = r.read()
    lexer.start_row_pos = 0
    lexer.input(data)
    with open('result.txt', 'w') as w:
        res = parser.parse()
        w.write(str(res))
