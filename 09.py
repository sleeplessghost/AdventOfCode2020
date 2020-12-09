from itertools import combinations

def findInvalid(numbers, pSize):
    preamble = numbers[:pSize]
    for n in numbers[pSize:]:
        combs = combinations(preamble, 2)
        if any(sum(seq) == n for seq in combs):
            preamble.pop(0)
            preamble.append(n)
        else: return n

def findRange(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total = sum(numbers[i : j+1])
            if total > target: break
            if total == target: return numbers[i : j+1]

numbers = [int(n) for n in open('in/09.txt')]

invalid = findInvalid(numbers, 25)
contain = findRange(numbers, invalid)

print('part1:', invalid)
print('part2:', min(contain) + max(contain))