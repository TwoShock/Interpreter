from enum import Enum

class TokenType(Enum):
    INTEGER="int"
    FLOAT = "float"
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    LEFTPAREN = "("
    RIGHTPAREN = ")"
    BEGIN = "BEGIN"
    END = "END"
    ASSIGNMENT = ":="
    SEMICOLON = ';'
    DOT = "."
    ID = "ID"
    EOF = "EOF"


