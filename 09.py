from itertools import combinations

def findInvalid(numbers, pSize):
    preamble = []
    for n in numbers:
        if len(preamble) < pSize:
            preamble.append(n)
        else:
            combs = combinations(preamble, 2)
            if not any(sum(seq) == n for seq in combs):
                return n
            else:
                preamble = preamble[1:]
                preamble.append(n)

def findRange(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total = sum(numbers[i : j+1])
            if total > target: break
            if total == target: return numbers[i : j+1]

numbers = [int(n) for n in open('in/09.txt')]

part1 = findInvalid(numbers, 25)
containing = findRange(numbers, part1)

print('part1:', part1)
print('part2:', min(containing) + max(containing))