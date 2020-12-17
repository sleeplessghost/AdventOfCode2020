from copy import deepcopy
from itertools import product
from collections import defaultdict

def activeNeighbours(cube, coords):
    possibles = [[c-1,c,c+1] for c in coords]
    combinations = product(*possibles)
    return sum(cube[c] for c in combinations if c != coords)

def step(oldCube, scaleMin, scaleMax, dimensions):
    cube = deepcopy(oldCube)
    indices = list(range(scaleMin, scaleMax))
    for coords in product(*[indices for __ in range(dimensions)]):
        neighbours = activeNeighbours(oldCube, coords)
        if oldCube[coords]: cube[coords] = 2 <= neighbours <= 3
        else: cube[coords] = neighbours == 3
    return cube

def calcCube(inp, dimensions, depth):
    cube = defaultdict(bool)
    for y, line in enumerate(inp):
        for x, char in enumerate(line):
            coords = list((x,y))
            for __ in range(dimensions - 2): coords.append(0)
            cube[tuple(coords)] = True if char == '#' else False
    for i in range(depth):
        cube = step(cube, 0 - i - 1, len(inp) + i + 1, dimensions)
    return cube

inp = [list(line.strip()) for line in open('in/17.txt')]
print('part1:', sum(calcCube(inp, 3, 6).values()))
print('part2:', sum(calcCube(inp, 4, 6).values()))