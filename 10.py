from collections import defaultdict

adapters = sorted(set([int(n) for n in open('in/10.txt')]))
adapters.insert(0,0)
adapters.append(max(adapters) + 3)

ones = 0
threes = 0
for i in range(len(adapters) - 1):
    diff = adapters[i+1] - adapters[i]
    if diff == 1: ones += 1
    elif diff == 3: threes += 1
print('part1:', ones * threes)

#paths to N = sum of paths to all adapters that can connect to N
#adapter can connect to N if it is 1/2/3 jolts lower rated
#must start at outlet 0 => 1 path
pathLengths = defaultdict(int)
pathLengths[0] = 1
for value in adapters[1:]:
    pathLengths[value] = sum(pathLengths[value - x] for x in [1, 2, 3])
lastPlug = adapters[-1]
print('part2:', pathLengths[lastPlug])