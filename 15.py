def runToNumber(numbers, target):
    mapped = {number: [index] for index, number in enumerate(numbers)}
    lastNumber, count = numbers[-1], len(numbers)
    while count < target:
        prev = mapped[lastNumber]
        if len(prev) < 2:
            lastNumber = 0
        else:
            secondMost, recent = prev[-2:]
            lastNumber = recent - secondMost
        if lastNumber not in mapped:
            mapped[lastNumber] = []
        mapped[lastNumber].append(count)
        count += 1
    return lastNumber

numbers = [int(n) for n in open('in/15.txt').read().split(',')]

print('part1:', runToNumber(numbers, 2020))
print('part2:', runToNumber(numbers, 30000000))
