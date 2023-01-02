from Token import Token
from TokenType import TokenType
from typing import List
from constants import DIGITS
RESERVED_KEYWORDS = {
    'BEGIN':Token(TokenType.BEGIN),
    'END':Token(TokenType.END)
}
class Lexer:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.pos: int = 0
        self.currentCharacter: chr = self.text[self.pos]

    def advance(self):
        self.pos += 1
        self.currentCharacter = self.text[self.pos] if self.pos <= len(
            self.text) - 1 else None
    def peek(self):
        nextPos = self.pos + 1
        if nextPos > len(self.text) -1:
            return None
        return self.text[nextPos]
    def _id(self)->Token:
        result = ''
        while self.currentCharacter!= None and self.currentCharacter.isalnum():
            result += self.currentCharacter
            self.advance()
        token:Token = RESERVED_KEYWORDS.get(result,Token(TokenType.ID,result))
        return token

    def makeTokens(self) -> list[Token]:
        tokens: list[Token] = []
        while self.currentCharacter != None:
            if self.currentCharacter in ' \t':
                self.advance()
            elif self.currentCharacter.isalpha():
                tokens.append(self._id())
            elif self.currentCharacter == ":" and self.peek() == '=':
                self.advance()
                self.advance()
                tokens.append(Token(TokenType.ASSIGNMENT))
            elif self.currentCharacter == ';':
                self.advance()
                tokens.append(Token(TokenType.SEMICOLON))
            elif self.currentCharacter == ".":
                self.advance()
                tokens.append(Token(TokenType.DOT))
            elif self.currentCharacter == '+':
                tokens.append(Token(TokenType.PLUS))
                self.advance()
            elif self.currentCharacter == '-':
                tokens.append(Token(TokenType.MINUS))
                self.advance()
            elif self.currentCharacter == '*':
                tokens.append(Token(TokenType.MULTIPLY))
                self.advance()
            elif self.currentCharacter == '/':
                tokens.append(Token(TokenType.DIVIDE))
                self.advance()
            elif self.currentCharacter == '(':
                tokens.append(Token(TokenType.LEFTPAREN))
                self.advance()
            elif self.currentCharacter == ')':
                tokens.append(Token(TokenType.RIGHTPAREN))
                self.advance()
            elif self.currentCharacter.isdigit():
                tokens.append(self.makeNumberToken())
            else:
                self.error()
        tokens.append(Token(TokenType.EOF))
        return tokens

    def makeNumberToken(self) -> Token:
        number: str = ''
        dotCount: int = 0
        while self.currentCharacter != None and self.currentCharacter in DIGITS + '.':
            if self.currentCharacter == ".":
                if dotCount == 1:
                    break
                dotCount += 1
                number += self.currentCharacter
            else:
                number += self.currentCharacter
            self.advance()

        if dotCount == 0:
            return Token(TokenType.INTEGER, int(number))
        else:
            return Token(TokenType.FLOAT, float(number))

    def error(self):
        raise Exception("Error parsing input")
