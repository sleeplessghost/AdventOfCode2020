from math import prod
from itertools import combinations

def calcA(numbers):
    for i, a in enumerate(numbers):
        for b in numbers[i+1:]:
            if a + b == 2020: return a * b

def calcB(numbers):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i+1:], i+1):
            for c in numbers[j+1:]:
                if a + b + c == 2020: return a * b * c

numbers = [int(n) for n in open('in/01.txt')]

print('two numbers sum to 2020 gives:', calcA(numbers))
print('three numbers sum to 2020 gives:', calcB(numbers))

##################################################################################

def calcProductFor(numbers, count, target):
    for seq in combinations(numbers, count):
        if sum(seq) == target: return prod(seq)

print('two numbers sum to 2020 gives:', calcProductFor(numbers, 2, 2020))
print('three numbers sum to 2020 gives:', calcProductFor(numbers, 3, 2020))