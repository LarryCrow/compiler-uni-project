import ply.lex as lex
from tokens import *
import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-parameters')

    return parser


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
lexer = lex.lex()
with open('sample.doh', 'r', encoding="UTF-8") as f:
    data = f.read()
    lexer.pos_in_line = 0
    lexer.input(data)

    tokens = []
    symbol_counter = 0
    for lexeme in lexer:
        if lexeme.type != 'NEWLINE':
            tokens.append(lexeme)
            print('LexToken(' + lexeme.type + ',' + lexeme.value + ',' + str(lexeme.lineno) + ','
              + str(lexeme.lexpos - symbol_counter) + ')')
        if re.match(r'NEWLINE', lexeme.type):
            symbol_counter = lexeme.lexpos + 1
        if re.match(r'COMMENT', lexeme.type):
            symbol_counter = lexeme.lexpos + len(lexeme.value)
