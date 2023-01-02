from Token import Token
from TokenType import TokenType
from Nodes.NumberNode import NumberNode
from Nodes.NoOpNode import NoOpNode
from Nodes.CompundNode import CompoundNode
from Nodes.AssignmentNode import AssignmentNode
from Nodes.VariableNode import VariableNode
from Nodes.BinaryOperatorNode import BinaryOperatorNode
from Nodes.UnaryOperatorNode import UnaryOperatorNode


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens: list[Token] = tokens
        self.tokenIndex: int = -1
        self.advance()

    def advance(self) -> Token:
        self.tokenIndex += 1
        if self.tokenIndex < len(self.tokens):
            self.currentToken: Token = self.tokens[self.tokenIndex]
        return self.currentToken

    def program(self):
        """program: compound_statement DOT"""
        node = self.compoundStatement()
        dot = self.currentToken
        self.advance()
        return node
    def statementList(self):
        """
        statmentList: statement | statment SEMI statement_list
        """
        node = self.statement()
        results = [node]
        while self.currentToken.type == TokenType.SEMICOLON:
            self.advance()
            results.append(self.statement())
        return results

    def statement(self):
       """
       statement: compound_statment| assignment statment | empty
       """ 
       node = None
       if self.currentToken.type == TokenType.BEGIN:
           node = self.compoundStatement()
       elif self.currentToken.type == TokenType.ID:
            node = self.assignmentStatement()
       else:
           node = self.empty()
       return node
        

    def assignmentStatement(self):
        left = self.variable()
        assignmentToken = self.currentToken
        self.advance()
        right = self.expr()
        node = AssignmentNode(left,assignmentToken,right)
        return node

    def variable(self):
        """
        variable: ID
        """
        node = VariableNode(self.currentToken)
        self.advance()
        return node 

    def compoundStatement(self):
        beginNode = self.currentToken
        self.advance()
        nodes = self.statementList()
        endNode = self.currentToken
        self.advance()
        root = CompoundNode()
        for node in nodes:
            root.children.append(node)
        return root


    def empty(self):
        return NoOpNode()

    def term(self):
        left = self.factor()
        while self.currentToken.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            operator: Token = self.currentToken
            self.advance()
            right = self.factor()
            left = BinaryOperatorNode(left, operator, right)
        return left

    def expr(self):
        left = self.term()
        while self.currentToken.type in (TokenType.PLUS, TokenType.MINUS):
            operator: Token = self.currentToken
            self.advance()
            right = self.term()
            left = BinaryOperatorNode(left, operator, right)
        return left

    def factor(self):
        token: Token = self.currentToken
        if token.type in (TokenType.PLUS, TokenType.MINUS):
            self.advance()
            factor = self.factor()
            return UnaryOperatorNode(token, factor)
        elif token.type in (TokenType.INTEGER, TokenType.FLOAT):
            self.advance()
            return NumberNode(token)
        elif token.type == TokenType.LEFTPAREN:
            self.advance()
            expression = self.expr()
            self.advance()
            return expression
        else:
            node = self.variable()
            return node
    def parse(self):
        node = self.program()
        return node