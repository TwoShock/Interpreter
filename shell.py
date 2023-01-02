from Lexer import Lexer
from Token import Token
from Parser import Parser
from Interpreter import Interpreter
from typing import List
while True:
    text:str = input(">")
    try:
        lexer = Lexer(text=text)
        tokens:List[Token] = lexer.makeTokens()
        #print(tokens)


        parser = Parser(tokens)
        print(parser.parse())

        # interpreter = Interpreter()
        # print(interpreter.visit(parser.expr()))


    except Exception:
        print("uh oh")