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
    lexer.pos_in_line = 0
    lexer.input(data)

    #tokens = []
    #symbol_counter = 0
    # for lexeme in lexer:
    #     if lexeme.type != 'NEWLINE':
    #         tokens.append(lexeme)
    #         print('LexToken(' + lexeme.type + ',' + lexeme.value + ',' + str(lexeme.lineno) + ','
    #           + str(lexeme.lexpos - symbol_counter) + ')')
    #     if re.match(r'NEWLINE', lexeme.type):
    #         symbol_counter = lexeme.lexpos + 1
    #     if re.match(r'COMMENT', lexeme.type):
    #         symbol_counter = lexeme.lexpos + len(lexeme.value)
    w = open('result.txt', 'w')
    res = parser.parse()
    w.write(str(res))
