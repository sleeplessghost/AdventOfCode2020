lines = [line.strip() for line in open('in/13.txt')]
timestamp = int(lines[0])
buses = [(i, int(t)) for i,t in enumerate(lines[1].split(',')) if t != 'x']

times = [(time, (time - timestamp) % time) for i, time in buses]
timeForLowest, lowestDifference = min(times, key=lambda x: x[1])
print('part1:', timeForLowest * lowestDifference)

result, product = 0,1
for i,time in buses:
    while (result + i) % time != 0:
        result += product
    product *= time
print('part2:', result)
