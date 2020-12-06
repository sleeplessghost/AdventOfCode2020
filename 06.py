from functools import reduce

def makeSets(group):
    return [set(line) for line in group.splitlines()]

def union(sets):
    return reduce(set.union, sets)

def intersect(sets):
    return reduce(set.intersection, sets)

text = open('in/06.txt').read()
groups = [makeSets(group) for group in text.split('\n\n')]

print('part1:', sum([len(union(g)) for g in groups]))
print('part2:', sum([len(intersect(g)) for g in groups]))