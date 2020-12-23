class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def makeLinkedList(cups, extendTo=None):
    values = {}
    if extendTo != None:
        cups = cups + [*range(max(cups) + 1, extendTo + 1)]
    for c in cups:
        values[c] = Node(c)
    for i,c in enumerate(cups):
        node = values[c]
        node.next = values[cups[(i + 1) % len(cups)]]
    return values

def pickup(current):
    a = current.next
    b = a.next
    c = b.next
    return [a,b,c]

def step(llist, current, minimum, maximum):
    a,b,c = pickup(current)
    current.next = c.next
    removedVals = [node.value for node in [a,b,c]]
    dest = current.value - 1
    while dest in removedVals or dest < minimum:
        dest -= 1
        if dest < minimum: dest = maximum
    destNode = llist[dest]
    c.next = destNode.next
    destNode.next = a
    return current.next

def pr(llist):
    result = [1]
    start = llist[1]
    node = start.next
    while node.value != 1:
        result.append(str(node.value))
        node = node.next
    return result

def playGame(cups, stepCount, extendTo=None):
    minimum, maximum = min(cups), extendTo if extendTo != None else max(cups)
    llist = makeLinkedList(cups, extendTo)
    current = llist[cups[0]]
    for __ in range(stepCount):
        current = step(llist, current, minimum, maximum)
    return llist

cups = [int(char) for char in list(open('in/23.txt').read())]

llist = playGame(cups, 100)
print('part1:', ''.join(pr(llist)[1:]))

llist = playGame(cups, 10_000_000, 1_000_000)
start = llist[1]
print('part2:', start.next.value * start.next.next.value)