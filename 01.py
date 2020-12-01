from itertools import combinations
from functools import reduce

numbers = [int(n) for n in open('in/01.txt')]

def calcA(numbers):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if j <= i: continue
            if a + b == 2020: return a * b
    return -1

def calcB(numbers):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if j <= i: continue
            for k, c in enumerate(numbers):
                if k <= i or k <= j: continue
                if a + b + c == 2020: return a * b * c
    return -1

def combi(numbers, count, targetVal):
    for seq in combinations(numbers, count):
        if sum(seq) == targetVal: return reduce(lambda a,b : a*b, seq)

print('two numbers sum to 2020 gives: ', calcA(numbers))
print('three numbers sum to 2020 gives: ', calcB(numbers))

print('two numbers sum to 2020 gives: ', combi(numbers, 2, 2020))
print('three numbers sum to 2020 gives: ', combi(numbers, 3, 2020))