def parseLine(line):
    direction = line[0]
    distance = int(line[1:])
    return direction, distance

values = [parseLine(line.strip()) for line in open('in/12.txt')]

x, y = (0,0)
currentDir = 90
for direction, distance in values:
    if direction == 'L': currentDir = (currentDir - distance) % 360
    if direction == 'R': currentDir = (currentDir + distance) % 360
    if direction == 'N' or (direction == 'F' and currentDir == 0): y += distance
    if direction == 'S' or (direction == 'F' and currentDir == 180): y -= distance
    if direction == 'E' or (direction == 'F' and currentDir == 90): x += distance
    if direction == 'W' or (direction == 'F' and currentDir == 270): x -= distance

print('part1:', abs(x) + abs(y))

x, y = (10,1)
sx, sy = (0,0)
for direction, distance in values:
    if direction == 'L' or direction == 'R':
        directed = distance if direction == 'R' else -distance
        absolute = directed % 360
        if absolute == 90: x,y = y,-x
        if absolute == 180: x,y = -x,-y
        if absolute == 270: x,y = -y,x
    if direction == 'N': y += distance
    if direction == 'S': y -= distance
    if direction == 'E': x += distance
    if direction == 'W': x -= distance
    if direction == 'F':
        sx += distance * x
        sy += distance * y

print('part2:', abs(sx) + abs(sy))