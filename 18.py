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
    match = re.search(r'(\d+ \+ \d+)', expr)
    while match:
        m = match.group()
        expr = expr.replace(m, str(ltr(m)), 1)
        match = re.search(r'(\d+ \+ \d+)', expr)
    return ltr(expr)

def evaluate(expr, additionFirst):
    while '(' in expr:
        matches = re.findall(r'(\([0-9\+\*\s]+\))', expr)
        for match in matches:
            if additionFirst: expr = expr.replace(match, str(additions(match[1:-1])))
            else: expr = expr.replace(match, str(ltr(match[1:-1])))
    return additions(expr) if additionFirst else ltr(expr)

lines = [line.strip() for line in open('in/18.txt')]

print('part1:', sum(evaluate(line, False) for line in lines))
print('part2:', sum(evaluate(line, True) for line in lines))