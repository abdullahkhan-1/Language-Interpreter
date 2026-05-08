import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run(filename):
    with open(filename, 'r') as f:
        code = f.read()

    tokens = Lexer(code).tokenize()
    ast    = Parser(tokens).parse()
    Interpreter().run(ast)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <filename.ms>')
    else:
        run(sys.argv[1])