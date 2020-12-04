from math import prod
from itertools import combinations

def calcProductFor(numbers, count, target):
    for seq in combinations(numbers, count):
        if sum(seq) == target: return prod(seq)

numbers = [int(n) for n in open('in/01.txt')]
print('part1:', calcProductFor(numbers, 2, 2020))
print('part2:', calcProductFor(numbers, 3, 2020))