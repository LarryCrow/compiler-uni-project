import ply.lex as lex
from tokens import *
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-parameters')

    return parser

lexer = lex.lex()

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
# namespace.parameters
with open(namespace.parameters, 'r', encoding="UTF-8") as f:
    data = f.read()
    lexer.input(data)

    tokens_arr = []

    for lexeme in lexer:
        tokens_arr.append(lexeme)
        print(lexeme)