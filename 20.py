from math import sqrt, prod

ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270 = 0,1,2,3
UNFLIPPED, FLIPPED = 0,1
TOP, RIGHT, BOTTOM, LEFT = 0,1,2,3

def parseTiles(tiles):
    result = {}
    for tile in tiles:
        lines = [line.strip() for line in tile.split('\n')]
        number = int(lines[0].split(' ')[1][:-1])
        mapped = [list(line) for line in lines[1:]]
        result[number] = mapped
    return result

def rotate(tile):
    return list(zip(*tile[::-1]))

def flip(tile):
    return tile[::-1]

def findEdges(tiles):
    result = {TOP:{}, RIGHT:{}, BOTTOM:{}, LEFT:{}}
    for number in tiles:
        pushSides(result, number, tiles[number])
    return result

def pushSides(dictionary, number, tile):
    t = tile
    for rotation in [ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270]:
        flipped = t
        for orientation in [UNFLIPPED, FLIPPED]:
            top, bottom, left, right = getSides(flipped)
            addSide(dictionary, TOP, rotation, orientation, number, top)
            addSide(dictionary, BOTTOM, rotation, orientation, number, bottom)
            addSide(dictionary, LEFT, rotation, orientation, number, left)
            addSide(dictionary, RIGHT, rotation, orientation, number, right)
            flipped = flip(t)
        t = rotate(t)

def addSide(dictionary, direction, rotation, orientation, number, value):
    if value not in dictionary[direction]:
        dictionary[direction][value] = []
    dictionary[direction][value].append((number, rotation, orientation))

def getSides(tile):
    top, bottom = ''.join(tile[0]), ''.join(tile[-1])
    left = ''.join([tile[y][0] for y in range(len(tile))])
    right = ''.join([tile[y][len(tile) - 1] for y in range(len(tile))])
    return top, bottom, left, right

def removeEdges(tile):
    return [line[1:-1] for line in tile[1:-1]]

def isMonster(image, x, y):
    positions = [(x,y), (x-18, y+1), (x-13, y+1), (x-12, y+1), (x-7, y+1), (x-6, y+1), (x-1, y+1), (x, y+1), (x+1, y+1), (x-17, y+2), (x-14, y+2), (x-11, y+2), (x-8, y+2), (x-5, y+2), (x-2, y+2)]
    return all(0 <= x < len(image) and 0 <= y < len(image) for (x,y) in positions) and all(image[y][x] == '#' for (x,y) in positions)
    

tiles = parseTiles(open('in/20.txt').read().split('\n\n'))
possibleEdges = findEdges(tiles)
edges = []
for edge in possibleEdges[TOP]:
    for number, rotation, orientation in possibleEdges[TOP][edge]:
        filtered = [(n, r, o) for n,r,o in possibleEdges[BOTTOM][edge] if n != number]
        if len(filtered) == 0 and number not in edges: edges.append(number)

nonMatches = {}
for number in edges:
    tile = tiles[number]
    tops = []
    nonMatches[number] = 0
    for val in possibleEdges[TOP]:
        matchedForVal = possibleEdges[TOP][val]
        for n, rotation, orientation in matchedForVal:
            if n == number: tops.append(val)
    for val in tops:
        matchingBottoms = [x for x in possibleEdges[BOTTOM][val] if x[0] != number]
        if len(matchingBottoms) == 0: nonMatches[number] += 1
corners = [x for x in nonMatches if nonMatches[x] == 4]
print('part1:', prod(corners))

topLeft = corners[0]
used = [topLeft]
tile = tiles[topLeft]
for rotation in [ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270]:
    top, bottom, left, right = getSides(tile)
    matchingBottoms = [x for x in possibleEdges[BOTTOM][top] if x[0] != topLeft]
    matchingRights = [x for x in possibleEdges[RIGHT][left] if x[0] != topLeft]
    if len(matchingBottoms) == 0 and len(matchingRights) == 0:
        break
    else: tile = rotate(tile)

full = [tile]
size = len(tiles)
length = int(sqrt(size))
current = topLeft
for y in range(length):
    for x in range(length):
        index = (y * length) + (x % length)
        if index == 0: continue
        if index % length == 0:
            tile = full[index - length]
            current = used[index - length]
            top, bottom, left, right = getSides(tile)
            matchingTop = [e for e in possibleEdges[TOP][bottom] if e[0] not in used][0]
            tile = tiles[matchingTop[0]]
            for rotates in range(matchingTop[1]):
                tile = rotate(tile)
            for flips in range(matchingTop[2]):
                tile = flip(tile)
            full.append(tile)
            used.append(matchingTop[0])
            current = matchingTop[0]
        else:
            top, bottom, left, right = getSides(tile)
            matchingLeft = [e for e in possibleEdges[LEFT][right] if e[0] not in used][0]
            tile = tiles[matchingLeft[0]]
            for rotates in range(matchingLeft[1]):
                tile = rotate(tile)
            for flips in range(matchingLeft[2]):
                tile = flip(tile)
            full.append(tile)
            used.append(matchingLeft[0])
            current = matchingLeft[0]

full = [removeEdges(tile) for tile in full]
reassembled = []
for i in range(0, len(full), length):
    for row in range(len(full[i])):
        newRow = ''.join([''.join(full[i + increment][row]) for increment in range(0, length)])
        reassembled.append(list(newRow))

hashCount = sum(sum(c == '#' for c in line) for line in reassembled)
monsterCount = 0
for rotation in [ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270]:
    for orientation in [UNFLIPPED, FLIPPED]:
        monsters = sum(isMonster(reassembled, x, y) for x in range(len(reassembled)) for y in range(len(reassembled)))
        monsterCount = max(monsterCount, monsters)
        reassembled = flip(reassembled)
    reassembled = rotate(reassembled)
print('part2:', hashCount - (15 * monsterCount))