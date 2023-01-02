from TokenType import TokenType


class Token:
    def __init__(self, type: TokenType, value: str = None) -> None:
        self.type: TokenType = type
        self.value: str = value

    def __str__(self) -> str:
        if self.value:
            return f'Token({self.type},{self.value})'
        else:
            return f'Token({self.type})'


    def __repr__(self) -> str:
        return self.__str__()
