import math

lines = [line.strip() for line in open('in/13.txt')]
timestamp = int(lines[0])
times = lines[1].split(',')
buses = [(i, int(t)) for i,t in enumerate(times) if t != 'x']

lowest = 888888
busId = -1
for i, t in buses:
    above = math.ceil(timestamp / t) * t
    diff = above - timestamp
    if diff < lowest:
        lowest = diff
        busId = t

print(busId * lowest)

result, product = 0,1
for i,time in buses:
    while (result + i) % time != 0:
        result += product
    product *= time
print(result)
