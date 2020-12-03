map = [line.strip() for line in open('in/03.txt') if line]

def countTrees(dx, dy):
    y, x, trees, lengthY, lengthX = 0, 0, 0, len(map), len(map[0])
    while y < lengthY:
        if map[y][x] == '#': trees += 1
        y += dy
        x  = (x + dx) % lengthX
    return trees

a = countTrees(1,1)
b = countTrees(3,1)
c = countTrees(5,1)
d = countTrees(7,1)
e = countTrees(1,2)
print('part1:', countTrees(3,1))
print('part2:', a * b * c * d * e)