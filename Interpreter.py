from Nodes.NumberNode import NumberNode
from TokenType import TokenType
from Nodes.BinaryOperatorNode import BinaryOperatorNode
from Nodes.UnaryOperatorNode import UnaryOperatorNode


class Number:
    def __init__(self, value) -> None:
        self.value = value

    def add(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)

    def sub(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)

    def mult(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)

    def div(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)

    def __repr__(self) -> str:
        return f'{self.value}'


class Interpreter:
    def visit(self, node):
        if type(node) == BinaryOperatorNode:
            return self.visitBinaryOperatorNode(node)
        elif type(node) == NumberNode:
            return self.visitNumberNode(node)
        elif type(node) == UnaryOperatorNode:
            return self.visitUnaryOperatorNode(node)
        else:
            self.noVisitMethod(node)


    def noVisitMethod(self, node):
        raise Exception("Interpreter: No visit method defined for node")

    def visitUnaryOperatorNode(self, node):
        number: Number = self.visit(node.node)
        if node.operator.type == TokenType.MINUS:
            number = number.mult(Number(-1))
        return number

    def visitBinaryOperatorNode(self, node):
        left: Number = self.visit(node.left)
        right: Number = self.visit(node.right)
        if node.operator.type == TokenType.PLUS:
            return Number(left.value + right.value)
        elif node.operator.type == TokenType.MINUS:
            return Number(left.value - right.value)
        elif node.operator.type == TokenType.MULTIPLY:
            return Number(left.value * right.value)
        elif node.operator.type == TokenType.DIVIDE:
            return Number(left.value / right.value)

    def visitNumberNode(self, node: NumberNode):
        return Number(node.token.value)
