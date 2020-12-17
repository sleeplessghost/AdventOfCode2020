from copy import deepcopy
from itertools import product

def activeNeighbours(cube, x, y, z, w):
    count = 0
    possibles = [[x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1], [w-1, w, w+1]]
    combinations = product(*possibles)
    for cx, cy, cz, cw in combinations:
        if not (cx == x and cy == y and cz == z and cw == w):
            if 0 <= cx < size and 0 <= cy < size and 0 <= cz < size and 0 <= cw < size:
                count += cube[cx][cy][cz][cw]
    return count

def step(oldCube):
    cube = deepcopy(oldCube)
    for x in range(len(cube)):
        for y in range(len(cube[x])):
            for z in range(len(cube[x][y])):
                for w in range(len(cube[x][y][z])):
                    neighbours = activeNeighbours(oldCube, x, y, z, w)
                    if oldCube[x][y][z][w]: cube[x][y][z][w] = 2 <= neighbours <= 3
                    else: cube[x][y][z][w] = neighbours == 3
    return cube

inp = [list(line.strip()) for line in open('in/17.txt')]
size = 30
offset = 12
zoffset = 15
cube = [[[[False for x in range(size)] for y in range(size)] for z in range(size)] for w in range(size)]

for i, line in enumerate(inp):
    for j, char in enumerate(line):
        cube[offset + j][offset + i][zoffset][zoffset] = True if char == '#' else False

for i in range(6):
    cube = step(cube)

result = 0
for x in range(len(cube)):
    for y in range(len(cube[x])):
        for z in range(len(cube[x][y])):
            for w in range(len(cube[x][y][z])):
                result += cube[x][y][z][w]
print(result)