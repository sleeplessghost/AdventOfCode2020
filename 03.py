def countTrees(dx, dy, map):
    y, x, trees, lengthY, lengthX = 0, 0, 0, len(map), len(map[0])
    while y < lengthY:
        if map[y][x] == '#': trees += 1
        y += dy
        x  = (x + dx) % lengthX
    return trees

map = [line.strip() for line in open('in/03.txt')]

print('part1:', countTrees(3,1, map))
a = countTrees(1,1, map)
b = countTrees(3,1, map)
c = countTrees(5,1, map)
d = countTrees(7,1, map)
e = countTrees(1,2, map)
print('part2:', a * b * c * d * e)