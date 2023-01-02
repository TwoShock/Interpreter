class AssignmentNode:
    def __init__(self,left,op,right) -> None:
        self.left = left
        self.token = self.op = op
        self.right = right

    def __repr__(self) -> str:
        return f'Assign({self.left}{self.right})'
        