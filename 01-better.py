from math import prod
from itertools import combinations

def calcProductFor(numbers, count, target):
    for seq in combinations(numbers, count):
        if sum(seq) == target: return prod(seq)

numbers = [int(n) for n in open('in/01.txt')]
print('two numbers sum to 2020 gives:', calcProductFor(numbers, 2, 2020))
print('three numbers sum to 2020 gives:', calcProductFor(numbers, 3, 2020))