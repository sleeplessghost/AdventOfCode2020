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

def step(oldCube, scaleMin, scaleMax, dimensions):
    cube = deepcopy(oldCube)
    indices = list(range(scaleMin, scaleMax))
    for coords in product(*[indices for __ in range(dimensions)]):
        neighbours = activeNeighbours(oldCube, coords)
        if oldCube[coords]: cube[coords] = 2 <= neighbours <= 3
        else: cube[coords] = neighbours == 3
    return cube

inp = [list(line.strip()) for line in open('in/17.txt')]

cube = defaultdict(bool)
for y, line in enumerate(inp):
    for x, char in enumerate(line):
        cube[(x,y,0)] = True if char == '#' else False

for i in range(6): cube = step(cube, 0 - i - 1, len(inp) + i + 1, 3)
print('part1:', sum(cube.values()))

cube = defaultdict(bool)
for y, line in enumerate(inp):
    for x, char in enumerate(line):
        cube[(x,y,0,0)] = True if char == '#' else False

for i in range(6): cube = step(cube, 0 - i - 1, len(inp) + i + 1, 4)
print('part2:', sum(cube.values()))