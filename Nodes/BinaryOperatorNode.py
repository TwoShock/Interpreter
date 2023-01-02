import sys
import os
sys.path.append(os.path.abspath(os.path.join("..", 'Mercury')))
# fmt: off
import Token
# fmt: on


class BinaryOperatorNode:
    def __init__(self, left: Token, operator: Token, right: Token) -> None:
        self.left: Token = left
        self.operator: Token = operator
        self.right: Token = right
        

    def __repr__(self) -> str:
        return f"({self.left}{self.operator}{self.right})"
