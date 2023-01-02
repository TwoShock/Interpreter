import sys
import os
sys.path.append(os.path.abspath(os.path.join("..", 'Mercury')))
# fmt: off
import Token
# fmt: on

class VariableNode:
    def __init__(self,token:Token) -> None:
        self.token:Token = token 
        self.value = token.value
    def __repr__(self) -> str:
        return f'Var({self.token},{self.value})'
        