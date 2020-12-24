from collections import defaultdict
import re

def parseLine(line):
    return re.findall('sw|se|nw|ne|e|w', line)

def getAdjacentPositions(x,y):
    return [(x-2,y), (x+2,y), (x-1,y+1), (x-1,y-1), (x+1,y+1), (x+1,y-1)]

def adjacent(tiles, x, y):
    return sum(tiles[pos] for pos in getAdjacentPositions(x,y))

def step(tiles):
    newTiles = tiles.copy()
    tilesToCheck = [[(x,y)] + getAdjacentPositions(x,y) for (x,y) in tiles.keys() if tiles[(x,y)]]
    tilesToCheck = set([pos for array in tilesToCheck for pos in array])
    for (x,y) in tilesToCheck:
        adj = adjacent(tiles, x, y)
        if tiles[(x,y)] and (adj == 0 or adj > 2): newTiles[(x,y)] = False
        elif not tiles[(x,y)] and adj == 2: newTiles[(x,y)] = True
    return newTiles

def countBlacks(tiles):
    return sum(tiles.values())

instructions = [parseLine(line.strip()) for line in open('in/24.txt')]
tiles = defaultdict(bool)

for instruction in instructions:
    x,y = 0,0
    for direction in instruction:
        if direction == 'e': x += 2
        elif direction == 'w': x -= 2
        else:
            if 'e' in direction: x += 1
            elif 'w' in direction: x -= 1
            if 's' in direction: y -= 1
            elif 'n' in direction: y += 1
    tiles[(x,y)] = not tiles[(x,y)]
print('part1:', countBlacks(tiles))

for i in range(100):
    tiles = step(tiles)
print('part2:', countBlacks(tiles))