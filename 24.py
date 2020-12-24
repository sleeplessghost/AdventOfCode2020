from collections import defaultdict

def parseLine(line):
    instructions = []
    i = 0
    while i < len(line):
        c0 = line[i]
        if c0 == 's' or c0 == 'n':
            instructions.append(c0 + line[i+1])
            i += 2
        else:
            instructions.append(c0)
            i += 1
    return instructions

def getAdjacentPositions(x,y):
    return [(x-2,y), (x+2,y), (x-1,y+1), (x-1,y-1), (x+1,y+1), (x+1,y-1)]

def adjacent(tiles, x, y):
    return sum(tiles[(xx,yy)] for xx,yy in getAdjacentPositions(x,y))

def step(tiles):
    newTiles = tiles.copy()
    blackTiles = [(x,y) for (x,y) in tiles.keys() if tiles[(x,y)]]
    tilesToCheck = blackTiles.copy()
    for (x,y) in blackTiles:
        tilesToCheck += getAdjacentPositions(x,y)
    tilesToCheck = set(tilesToCheck)
    for (x,y) in tilesToCheck:
        adj = adjacent(tiles, x, y)
        if tiles[(x,y)] and (adj == 0 or adj > 2):
            newTiles[(x,y)] = False
        if not tiles[(x,y)] and adj == 2:
            newTiles[(x,y)] = True
    return newTiles

def countBlacks(tiles):
    return sum(tiles.values())

instructions = [parseLine(line.strip()) for line in open('in/24.txt')]

tiles = defaultdict(bool)
for instruction in instructions:
    x,y = 0,0
    for instr in instruction:
        if instr == 'e': x += 2
        elif instr == 'w': x -= 2
        else:
            if 'e' in instr: x += 1
            elif 'w' in instr: x -= 1
            if 's' in instr: y -= 1
            elif 'n' in instr: y += 1
    tiles[(x,y)] = not tiles[(x,y)]
print('part1:', countBlacks(tiles))

for i in range(100):
    tiles = step(tiles)
print('part2:', countBlacks(tiles))