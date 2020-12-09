def lineToBinary(line):
    return line.replace('B','1').replace('F','0').replace('R','1').replace('L','0')

seats = [int(lineToBinary(line), 2) for line in open('in/05.txt')]

missingSeat = next(
    s for s in range(min(seats), max(seats))
    if (s not in seats))

print('part1:', max(seats))
print('part2:', missingSeat)