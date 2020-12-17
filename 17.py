from copy import deepcopy
from itertools import product

def activeNeighbours(cube, x, y, z):
    count = 0
    possibles = [[x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1]]
    combinations = product(*possibles)
    for cx, cy, cz in combinations:
        if not (cx == x and cy == y and cz == z):
            if 0 <= cx < size and 0 <= cy < size and 0 <= cz < size:
                count += cube[cx][cy][cz]
    return count

def step(oldCube):
    cube = deepcopy(oldCube)
    for x in range(len(cube)):
        for y in range(len(cube[x])):
            for z in range(len(cube[x][y])):
                neighbours = activeNeighbours(oldCube, x, y, z)
                if oldCube[x][y][z]: cube[x][y][z] = 2 <= neighbours <= 3
                else: cube[x][y][z] = neighbours == 3
    return cube

inp = [list(line.strip()) for line in open('in/17.txt')]
size = 30
offset = 12
zoffset = 15
cube = [[[False for x in range(size)] for y in range(size)] for z in range(size)]

for i, line in enumerate(inp):
    for j, char in enumerate(line):
        cube[offset + j][offset + i][zoffset] = True if char == '#' else False

for i in range(6):
    cube = step(cube)

result = 0
for x in range(len(cube)):
    for y in range(len(cube[x])):
        for z in range(len(cube[x][y])):
            result += cube[x][y][z]
print(result)