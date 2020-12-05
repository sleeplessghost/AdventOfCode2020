def lineToBinary(line):
    return line.replace('B','1').replace('F','0').replace('R','1').replace('L','0')

lines = [line.strip() for line in open('in/05.txt')]
seats = [int(lineToBinary(line), 2) for line in lines]

possibleSeats = range(0, int('1111111111', 2))
missingSeat = next(s for s in possibleSeats if (s not in seats and s-1 in seats and s+1 in seats))

print('part1:', max(seats))
print('part2:', missingSeat)