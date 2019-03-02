import ply.lex as lex
from tokens import *


lexer = lex.lex()

with open("sample.doh", 'r', encoding="UTF-8") as f:
    data = f.read()
    lexer.input(data)

    tokens_arr = []
    symbol_counter = 0

    for lexeme in lexer:
        print(lexeme)