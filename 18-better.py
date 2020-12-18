import re

class op(int):
    def __mul__(self, other): return op(int(self) + other)
    def __add__(self, other): return op(int(self) + other)
    def __sub__(self, other): return op(int(self) * other)

def evaluate(expr, additionFirst):
    expr = re.sub(r'(\d+)', r'op(\1)', expr)
    expr = expr.replace('*','-')
    if additionFirst: expr = expr.replace('+', '*')
    return eval(expr, {"op": op})

lines = [line.strip() for line in open('in/18.txt')]

print('part1:', sum(evaluate(line, False) for line in lines))
print('part2:', sum(evaluate(line, True) for line in lines))