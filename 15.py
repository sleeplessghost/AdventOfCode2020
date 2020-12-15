numbers = [int(n) for n in open('in/15.txt').read().split(',')]

mapped = {}
for i, n in enumerate(numbers):
    mapped[n] = [i]

lastNumber = numbers[-1]
count = len(numbers)
while count < 30000000:
    prev = mapped[lastNumber]
    if len(prev) < 2:
        lastNumber = 0
    else:
        first, second = prev[-2:]
        lastNumber = second - first
    if lastNumber not in mapped:
        mapped[lastNumber] = []
    mapped[lastNumber].append(count)
    count += 1
print(count, ':', lastNumber)