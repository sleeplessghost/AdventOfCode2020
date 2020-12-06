import functools

def setlines(group):
    return [set(line) for line in group.split('\n') if line]

def union(groupsets):
    return len(functools.reduce(lambda a,b : a.union(b), groupsets))

def intersect(groupsets):
    return len(functools.reduce(lambda a,b: a.intersection(b), groupsets))

input = open('in/06.txt').read()

grop = [setlines(group) for group in input.split('\n\n')]
print('part1:', sum([union(g) for g in grop]))
print('part2:', sum([intersect(g) for g in grop]))