numbers = []
for n in open('in/01.txt'):
    numbers.append(int(n))

def calcA(numbers):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if i == j: continue
            if a + b == 2020: return a * b
    return -1

def calcB(numbers):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if i == j: continue
            for k, c in enumerate(numbers):
                if i == k or j == k: continue
                if a + b + c == 2020: return a * b * c
    return -1


print('two numbers sum to 2020 gives: ', calcA(numbers))
print('three numbers sum to 2020 gives: ', calcB(numbers))