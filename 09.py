from itertools import combinations


numbers = [int(n) for n in open('in/09.txt')]

preamble = []
nf = None
for n in numbers:
    if len(preamble) < 25:
        preamble.append(n)
    else:
        combs = combinations(preamble, 2)
        if not any(sum(seq) == n for seq in combs):
            nf = n
            break
        preamble = preamble[1:]
        preamble.append(n)

print(nf)
rs = 0
re = 0
for i in range(len(numbers)):
    sum = numbers[i]
    for j in range(i+1, len(numbers)):
        sum += numbers[j]
        if sum == nf:
            print('range:', numbers[i], numbers[j])
            rs = i
            re = j
        elif sum > nf:
            break

r = numbers[rs:re+1]
print(rs, re)
print(r)
print(min(r), max(r))
print(min(r) + max(r))