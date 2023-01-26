from .base import AST, visualizer
import dtypes.ast as ast

class BinOp(AST):
    """
        Binary operator
    """
    def __new__(cls, right, left, **dict):
        return super().__new__(cls, f'{cls.__name__}_Node', right=right, left=left, **dict)

    def __init__(self, left, right):
        self.left = left
        self.right = right

class BitOr(BinOp):
    @visualizer
    def __eq__(self, other) -> AST:
        self.right = Eq(self.right, other)
        return self
    @visualizer
    def __ne__(self, other) -> AST:
        self.right = Ne(self.right, other)
        return self
    @visualizer
    def __lt__(self, other) -> AST:
        self.right = Lt(self.right, other)
        return self
    @visualizer
    def __gt__(self, other) -> AST:
        self.right = Gt(self.right, other)
        return self
    @visualizer
    def __le__(self, other) -> AST:
        self.right = Le(self.right, other)
        return self
    @visualizer
    def __ge__(self, other) -> AST:
        self.right = Ge(self.right, other)
        return self
    @visualizer
    def __and__(self, other) -> AST:
        self.right = And(self.right, other)
        return self

class And(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() and self.right.eval()
    @visualizer
    def __and__(self, other):
        return And(self, other)
    @visualizer
    def __or__(self, other):
        return Or(self, other)
    # @visualizer
    # def __rand__(self, other):
    #     return And(self, other)
    # @visualizer
    def __ror__(self, other):
        # print(self, other)
        return Or(self, other)

class Or(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() or self.right.eval()
    @visualizer
    def __and__(self, other):
        return And(self, other)
    @visualizer
    def __or__(self, other):
        return Or(self, other)
    # @visualizer
    # def __rand__(self, other):
    #     return And(self, other)
    @visualizer
    def __ror__(self, other):
        if isinstance(other, (int, float)):
            other = ast.Constant(other)
            return BitOr(other, self)

class Statement(BinOp):
    """
        Binary operator for declaring truth values.
    """
    @visualizer
    def __and__(self, other):
        return And(self, other)
    @visualizer
    def __or__(self, other):
        return Or(self, other)

    def __ror__(self, other):
        if isinstance(other, (int, float)):
            other = ast.Constant(other)
        return BitOr(other, self)

class Lt(Statement):...

class Gt(Statement):...

class Le(Statement):... 

class Ge(Statement):...

class Eq(Statement):...

class Ne(Statement):...

class Add(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() * self.right.eval()

class TrueDiv(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() / self.right.eval()

class FloorDiv(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval // self.right.eval()

class Mod(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() % self.right.eval()
    
class Pow(BinOp):
    @visualizer
    def eval(self):
        return self.left.eval() ** self.right.eval()
