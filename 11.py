from copy import deepcopy

def checkOccupied(row, column, direction, seats, adjacentOnly):
    rowChange, columnChange = direction
    r, c = row + rowChange, column + columnChange
    if not (0 <= r < len(seats) and 0 <= c < len(seats[0])): return False
    if seats[r][c] == '#': return True
    if seats[r][c] == 'L' or adjacentOnly: return False
    return checkOccupied(r, c, direction, seats, adjacentOnly)

def getCountAt(row, column, seats, adjacentOnly):
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    return sum(checkOccupied(row, column, direction, seats, adjacentOnly) for direction in directions)

def step(seats, adjacentOnly):
    result = deepcopy(seats)
    hasChanged = False
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            maxCount = 4 if adjacentOnly else 5
            count = getCountAt(row, column, seats, adjacentOnly)
            switchEmpty = seats[row][column] == 'L' and count == 0
            switchOccupied = seats[row][column] == '#' and count >= maxCount
            if switchEmpty: result[row][column] = '#'
            if switchOccupied: result[row][column] = 'L'
            if (switchEmpty or switchOccupied): hasChanged = True
    return hasChanged, result

def stepToEnd(seats, adjacentOnly):
    hasChanged, new = step(seats, adjacentOnly)
    while hasChanged:
        hasChanged, new = step(new, adjacentOnly)
    return new

seats = [list(line.strip()) for line in open('in/11.txt')]

part1 = stepToEnd(seats, True)
part2 = stepToEnd(seats, False)

print('part1:', sum(row.count('#') for row in part1))
print('part2:', sum(row.count('#') for row in part2))