def countTrees(dx, dy, map):
    x, trees, lengthY, lengthX = 0, 0, len(map), len(map[0])
    for y in range(0, lengthY, dy):
        if map[y][x] == '#': trees += 1
        x = (x + dx) % lengthX
    return trees

map = [line.strip() for line in open('in/03.txt')]

a = countTrees(1,1, map)
b = countTrees(3,1, map)
c = countTrees(5,1, map)
d = countTrees(7,1, map)
e = countTrees(1,2, map)

print('part1:', b)
print('part2:', a * b * c * d * e)