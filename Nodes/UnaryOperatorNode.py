import sys
import os
sys.path.append(os.path.abspath(os.path.join("..", 'Mercury')))
# fmt: off
import Token
# fmt: on

class UnaryOperatorNode:
    def __init__(self,operator:Token,node) -> None:
        self.operator:Token = operator
        self.node = node 

    def __repr__(self) -> str:
        return f"({self.operator}{self.node})"
        