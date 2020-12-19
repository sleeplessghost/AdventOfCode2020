from itertools import product

def parseRules(rules):
    result = {}
    for rule in rules.split('\n'):
        number, value = rule.split(': ')
        if '"' in value:
            value = value.replace('"','').strip()
        result[int(number)] = value
    return result

def pattern(rules, index):
    value = rules[index]
    if len(value) == 1 and not any(c.isdigit() for c in value):
        yield value
    else:
        options = value.split(' | ')
        for opt in options:
            patterns = [pattern(rules, int(i)) for i in opt.split(' ')]
            prod = product(*patterns)
            for combination in prod:
                yield ''.join(combination)

rules, messages = open('in/19.txt').read().split('\n\n')
rules = parseRules(rules)
patterns = [p for p in pattern(rules, 0)]

messages = messages.split('\n')
valid = [m for m in messages if m in patterns]
print('part1:', len(valid))

# rules[8] = '42 | 42 8'
# rules[11] = '42 31 | 42 11 31'

# patterns = [p for p in pattern(rules, 0)]
# valid = [m for m in messages if m in patterns]
# print('part2:', len(valid))