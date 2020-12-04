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
print('part1:', calcA(numbers))
print('part2:', calcB(numbers))