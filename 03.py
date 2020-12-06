def countTrees(dx, dy, chart):
    x, trees, lengthY, lengthX = 0, 0, len(chart), len(chart[0])
    for y in range(0, lengthY, dy):
        if chart[y][x] == '#': trees += 1
        x = (x + dx) % lengthX
    return trees

chart = [line.strip() for line in open('in/03.txt')]

a = countTrees(1,1, chart)
b = countTrees(3,1, chart)
c = countTrees(5,1, chart)
d = countTrees(7,1, chart)
e = countTrees(1,2, chart)

print('part1:', b)
print('part2:', a * b * c * d * e)