def runToNumber(numbers, target):
    mapped = {number: index for index, number in enumerate(numbers)}
    lastNumber = numbers[-1]
    for index in range(len(numbers), target):
        nextNumber, prevIndex = 0, index - 1
        if lastNumber in mapped:
            previous = mapped[lastNumber]
            nextNumber = prevIndex - previous
        mapped[lastNumber] = prevIndex
        lastNumber = nextNumber
    return lastNumber

numbers = [int(n) for n in open('in/15.txt').read().split(',')]

print('part1:', runToNumber(numbers, 2020))
print('part2:', runToNumber(numbers, 30000000))
