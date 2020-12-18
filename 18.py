import re

def op(total, value, operator):
    if operator == '+': return total + value
    elif operator == '-': return total - value
    elif operator == '*': return total * value

def evaluate(expr):
    while '(' in expr:
        start = expr.find('(') + 1
        end = 0
        sub = expr[start:]
        count = 1
        for i, c in enumerate(sub):
            if c == '(': count += 1
            elif c == ')': count -= 1
            if count == 0: 
                end = i
                break
        sub = sub[:end]
        end += start
        brack = evaluate(sub)
        expr = expr[:start-1] + str(brack) + expr[end+1:]
    result = None
    operator = '+'
    while '+' in expr:
        matches = re.findall(r'(\d+ \+ \d+)', expr)
        if matches is None: break
        match = matches[0]
        split = match.split(' + ')
        evald = int(split[0]) + int(split[1])
        start = expr.find(match)
        expr = expr[:start] + str(evald) + expr[start + len(match):]
    for token in expr.split(' '):
            if token in ['+','-','*']: operator = token
            elif result is None: result = int(token)
            else: result = op(result, int(token), operator)
    return result

lines = [line.strip() for line in open('in/18.txt')]

result = sum(evaluate(line) for line in lines)
print('part2:', result)