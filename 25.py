def transform(loopSize, subject):
    value = 1
    for __ in range(loopSize):
        value = (value * subject) % 20201227
    return value

a,b = [line.strip() for line in open('in/25.txt')]
a,b = int(a), int(b)

loop = None
value = 1
i = 1
while loop == None:
    value = (value * 7) % 20201227
    if value == a: loop = i
    else: i += 1

key = transform(loop, b)
print('part1:', key)
print('part2: freebie')