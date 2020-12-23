class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def makeLinkedList(cups, extendTo=None):
    if extendTo != None:
        cups += [*range(max(cups) + 1, extendTo + 1)]
    llist = {c: Node(c) for c in cups}
    length = len(cups)
    for i,c in enumerate(cups):
        node = llist[c]
        node.next = llist[cups[(i + 1) % length]]
    return llist

def step(llist, current, minimum, maximum):
    a,b,c = [current.next, current.next.next, current.next.next.next]
    removedVals = [node.value for node in [a,b,c]]
    dest = current.value - 1
    while dest in removedVals or dest < minimum:
        dest -= 1
        if dest < minimum: dest = maximum
    destNode = llist[dest]
    current.next = c.next
    c.next = destNode.next
    destNode.next = a
    return current.next

def playGame(cups, stepCount, extendTo=None):
    minimum, maximum = min(cups), max(cups) if extendTo == None else extendTo
    llist = makeLinkedList(cups, extendTo)
    current = llist[cups[0]]
    for __ in range(stepCount):
        current = step(llist, current, minimum, maximum)
    return llist

cups = [int(char) for char in list(open('in/23.txt').read())]

llist = playGame(cups, 100)
result, node = '', llist[1].next
while node.value != 1:
    result += str(node.value)
    node = node.next
print('part1:', result)

llist = playGame(cups, 10_000_000, 1_000_000)
start = llist[1]
print('part2:', start.next.value * start.next.next.value)