class CompoundNode:
    def __init__(self) -> None:
        """
        BEGIN ... END block
        """
        self.children:list = []
    def __repr__(self) -> str:
        result = "CompoundNode("

        for child in self.children:
            result += f'{child},'
        return f'{result})' 
            