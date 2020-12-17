from copy import deepcopy
from itertools import product
from collections import defaultdict

def activeNeighbours(cube, x, y, z):
    count = 0
    possibles = [[x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1]]
    combinations = product(*possibles)
    for cx, cy, cz in combinations:
        if not (cx == x and cy == y and cz == z):
            count += cube[cx][cy][cz]
    return count

def activeNeighbours2(cube, x, y, z, w):
    count = 0
    possibles = [[x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1], [w-1,w,w+1]]
    combinations = product(*possibles)
    for cx, cy, cz, cw in combinations:
        if not (cx == x and cy == y and cz == z and cw == w):
            count += cube[cx][cy][cz][cw]
    return count

def step(oldCube, scaleMin, scaleMax):
    cube = deepcopy(oldCube)
    for x in range(scaleMin, scaleMax):
        for y in range(scaleMin, scaleMax):
            for z in range(scaleMin, scaleMax):
                neighbours = activeNeighbours(oldCube, x, y, z)
                if oldCube[x][y][z]: cube[x][y][z] = 2 <= neighbours <= 3
                else: cube[x][y][z] = neighbours == 3
    return cube

def step2(oldCube, scaleMin, scaleMax):
    cube = deepcopy(oldCube)
    for x in range(scaleMin, scaleMax):
        for y in range(scaleMin, scaleMax):
            for z in range(scaleMin, scaleMax):
                for w in range(scaleMin, scaleMax):
                    neighbours = activeNeighbours2(oldCube, x, y, z, w)
                    if oldCube[x][y][z][w]: cube[x][y][z][w] = 2 <= neighbours <= 3
                    else: cube[x][y][z][w] = neighbours == 3
    return cube

inp = [list(line.strip()) for line in open('in/17.txt')]
size = len(inp)
cube = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))

for y, line in enumerate(inp):
    for x, char in enumerate(line):
        cube[x][y][0] = True if char == '#' else False

for i in range(6):
    cube = step(cube, 0 - i - 1, size + i + 1)

result = 0
for x in cube:
    for y in cube[x]:
        for z in cube[x][y]:
            result += cube[x][y][z]
print('part1:', result)

cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(bool))))

for y, line in enumerate(inp):
    for x, char in enumerate(line):
        cube[x][y][0][0] = True if char == '#' else False

for i in range(6):
    cube = step2(cube, 0 - i - 1, size + i + 1)

result = 0
for x in cube:
    for y in cube[x]:
        for z in cube[x][y]:
            for w in cube[x][y][z]:
                result += cube[x][y][z][w]
print('part2:', result)