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

print('two numbers sum to 2020 gives: ', calcA(numbers))
print('three numbers sum to 2020 gives: ', calcB(numbers))