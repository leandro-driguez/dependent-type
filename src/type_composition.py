from ast import parse
from visitor import CheckTypeComposition

def composes(dt_a, dt_b):
    """
        Dependent type A composes dependent type B.
    """
    ast_a = parse(dt_a)
    ast_b = parse(dt_b)

    ctx_a = {} 
    ctx_b = {}
    CheckTypeComposition().visit(ast_a, ctx_a)
    CheckTypeComposition().visit(ast_b, ctx_b)

    rng_a = ctx_a["x"]["range"]
    rng_b = ctx_b["x"]["range"]

    if rng_a is None:
        return True
    elif rng_b is None:
        return False

    u = rng_a | rng_b

    return rng_b == u

stament = composes(
    'List[int | (lambda x: x < 170 and x > 160)]',
    'List[float | (lambda x: x > 100 and x < 170)]'
)

print(stament)
