import re

def ltr(expr):
    result, operator = None, None
    for token in expr.split(' '):
        if token in ['+','*']: operator = token
        elif result is None: result = int(token)
        elif operator == '+': result += int(token)
        elif operator == '*': result *= int(token)
    return result

def additions(expr):
    additionMatch = re.search(r'(\d+ \+ \d+)', expr)
    while additionMatch:
        add = additionMatch.group()
        expr = expr.replace(add, str(ltr(add)), 1)
        additionMatch = re.search(r'(\d+ \+ \d+)', expr)
    return ltr(expr)

def evaluate(expr, additionFirst):
    while '(' in expr:
        bracketMatches = re.findall(r'(\([0-9\+\*\s]+\))', expr)
        for brackets in bracketMatches:
            if additionFirst: expr = expr.replace(brackets, str(additions(brackets[1:-1])))
            else: expr = expr.replace(brackets, str(ltr(brackets[1:-1])))
    return additions(expr) if additionFirst else ltr(expr)

lines = [line.strip() for line in open('in/18.txt')]

print('part1:', sum(evaluate(line, False) for line in lines))
print('part2:', sum(evaluate(line, True) for line in lines))