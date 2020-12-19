from itertools import product

def parseRules(rules):
    result = {}
    for rule in rules.split('\n'):
        index, value = rule.split(': ')
        if '"' in value:
            value = value.replace('"','').strip()
        result[int(index)] = value
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

def messageIsValid(message, ruleLeft, ruleRight):
    length = len(ruleLeft[0])
    chunks = [message[i:i+length] for i in range(0, len(message), length)]
    if all(c in ruleLeft or c in ruleRight for c in chunks):
        left = sum(c in ruleLeft for c in chunks)
        right = sum(c in ruleRight for c in chunks)
        if left > right and right > 0:
            firstRight = next(i for i,c in enumerate(chunks) if c in ruleRight)
            return all(c not in ruleLeft for c in chunks[firstRight + 1:])
    return False

rules, messages = open('in/19.txt').read().split('\n\n')
rules = parseRules(rules)
messages = messages.split('\n')

rule0 = [p for p in pattern(rules, 0)]
print('part1:', len([m for m in messages if m in rule0]))

rule42 = [p for p in pattern(rules, 42)]
rule31 = [p for p in pattern(rules, 31)]
print('part2:', sum(messageIsValid(m, rule42, rule31) for m in messages))