import sys
import os
sys.path.append(os.path.abspath(os.path.join("..", 'Mercury')))
# fmt: off
import Token
# fmt: on

class NumberNode:
    def __init__(self,token:Token) -> None:
        self.token:Token = token


    def __repr__(self) -> str:
        return f"{self.token}"
        