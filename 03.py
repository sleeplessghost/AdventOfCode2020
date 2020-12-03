from copy import deepcopy

lines = [line.strip() for line in open('in/03.txt') if line]
map = []

for row, line in enumerate(lines):
    map.append([])
    for c in line:
        map[row].append(c)

def checkFor(dx, dy):
    y, x, trees, length = 0, 0, 0, len(map[0])
    while y < len(map):
        if map[y][x] == '#': trees += 1
        y += dy
        x  = (x + dx) % length
    return trees

a = checkFor(1,1)
b = checkFor(3,1)
c = checkFor(5,1)
d = checkFor(7,1)
e = checkFor(1,2)
print('part1:', checkFor(3,1))
print('part2:', a * b * c * d * e)