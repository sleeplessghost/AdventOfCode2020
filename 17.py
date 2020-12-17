from copy import deepcopy
from itertools import product
from collections import defaultdict

def activeNeighbours(cube, coords):
    count = 0
    possibles = [[c-1,c,c+1] for c in coords]
    combinations = product(*possibles)
    for coordinates in combinations:
        if coordinates != coords:
            count += cube[coordinates]
    return count

def stepAtCoordinate(cube, oldCube, coords):
    neighbours = activeNeighbours(oldCube, coords)
    if oldCube[coords]: cube[coords] = 2 <= neighbours <= 3
    else: cube[coords] = neighbours == 3

def step(oldCube, scaleMin, scaleMax):
    cube = deepcopy(oldCube)
    for x in range(scaleMin, scaleMax):
        for y in range(scaleMin, scaleMax):
            for z in range(scaleMin, scaleMax):
                stepAtCoordinate(cube, oldCube, (x,y,z))
    return cube

def step2(oldCube, scaleMin, scaleMax):
    cube = deepcopy(oldCube)
    for x in range(scaleMin, scaleMax):
        for y in range(scaleMin, scaleMax):
            for z in range(scaleMin, scaleMax):
                for w in range(scaleMin, scaleMax):
                    stepAtCoordinate(cube, oldCube, (x,y,z,w))
    return cube

inp = [list(line.strip()) for line in open('in/17.txt')]
size = len(inp)
cube = defaultdict(bool)

for y, line in enumerate(inp):
    for x, char in enumerate(line):
        cube[(x,y,0)] = True if char == '#' else False

for i in range(6):
    cube = step(cube, 0 - i - 1, size + i + 1)

print('part1:', sum(cube.values()))

cube = defaultdict(bool)

for y, line in enumerate(inp):
    for x, char in enumerate(line):
        cube[(x,y,0,0)] = True if char == '#' else False

for i in range(6):
    cube = step2(cube, 0 - i - 1, size + i + 1)

print('part2:', sum(cube.values()))