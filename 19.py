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

r42 = [p for p in pattern(rules, 42)]
r31 = [p for p in pattern(rules, 31)]

count = 0
length = len(r42[0])
valids = []
for m in messages:
    orig = m
    while len(m) > 0:
        sub = m[:length]
        m = m[length:]
        if sub not in r42: break
        chunks = [m[i:i+length] for i in range(0, len(m), length)]
        left,right = 0,0
        for c in chunks:
            if c in r42:
                if right > 0:
                    left = -1
                    break
                else: left += 1
            elif c in r31:
                right += 1
            else:
                left = -1
                break
        if left == right and len(m) > 0: 
            valids.append(orig)
            break
print('part2:', len(valids))