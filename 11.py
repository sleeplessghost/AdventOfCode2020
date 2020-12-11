from copy import deepcopy

def checkOccupied(row, column, drow, dcol, seats):
    maxX = len(seats[0])
    maxY = len(seats)
    r = row + drow
    c = column + dcol
    if c < 0 or c >= maxX: return False
    if r < 0 or r >= maxY: return False
    if seats[r][c] == '#': return True
    if seats[r][c] == 'L': return False
    return checkOccupied(r, c, drow, dcol, seats)

def step(seats):
    result = deepcopy(seats)
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            left = checkOccupied(row, column, 0, -1, seats)
            right = checkOccupied(row, column, 0, 1, seats)
            up = checkOccupied(row, column, -1, 0, seats)
            down = checkOccupied(row, column, 1, 0, seats)
            UL = checkOccupied(row, column, -1, -1, seats)
            UR = checkOccupied(row, column, -1, 1, seats)
            DL = checkOccupied(row, column, 1, -1, seats)
            DR = checkOccupied(row, column, 1, 1, seats)
            count = sum([left, right, up, down, UL, UR, DL, DR])

            if seats[row][column] == 'L' and count == 0: result[row][column] = '#'
            if seats[row][column] == '#' and count >= 5: result[row][column] = 'L'
    return result

def isSame(a, b):
    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col] != b[row][col]: return False
    return True

seats = [list(line.strip()) for line in open('in/11.txt')]

old = seats
new = step(seats)
while not isSame(old, new):
    old = new
    new = step(new)

count = 0
for row in range(len(new)):
        for col in range(len(new[0])):
            if new[row][col] == '#': count += 1

print(count)
# for row in seats:
#     print(''.join(row))