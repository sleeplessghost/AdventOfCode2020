import re
from math import prod

def parseFieldRules(fieldRules):
    split = [re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rule).groups() for rule in fieldRules.splitlines()]
    return [(field, (int(lowerA), int(upperA)), (int(lowerB), int(upperB))) for field, lowerA, upperA, lowerB, upperB in split]

def parseNearbyTickets(nearbyTickets):
    split = [line.split(',') for line in nearbyTickets.splitlines()[1:]]
    return [[int(num) for num in arr] for arr in split]

def parseYourTicket(yourTicket):
    return [int(num) for num in yourTicket.splitlines()[1].split(',')]

def valuePassesRule(value, field, boundsA, boundsB):
    return boundsA[0] <= value <= boundsA[1] or boundsB[0] <= value <= boundsB[1]

def countInvalid(ticket, fieldRules):
    invalidValues = []
    for value in ticket:
        if not any(valuePassesRule(value, *field) for field in fieldRules): invalidValues.append(value)
    if len(invalidValues) > 0:
        return sum(invalidValues)

fieldRules, yourTicket, nearbyTickets = open('in/16.txt').read().split('\n\n')
fieldRules = parseFieldRules(fieldRules)
nearbyTickets = parseNearbyTickets(nearbyTickets)
yourTicket = parseYourTicket(yourTicket)

invalids = [countInvalid(ticket, fieldRules) for ticket in nearbyTickets]
print('part1:', sum(v for v in invalids if v is not None))

allFields = [field for field, boundsA, boundsB in fieldRules]
validPossibilities = {i:allFields.copy() for i,value in enumerate(nearbyTickets[0])}
nearbyTickets = [ticket for ticket in nearbyTickets if countInvalid(ticket, fieldRules) == None]
for ticket in nearbyTickets:
    for i,value in enumerate(ticket):
        for field, boundsA, boundsB in fieldRules:
            if field in validPossibilities[i] and not valuePassesRule(value, field, boundsA, boundsB):
                validPossibilities[i].remove(field)

while not all(len(validPossibilities[p]) == 1 for p in validPossibilities):
    allSingle = [i for i in validPossibilities if len(validPossibilities[i]) == 1]
    for current in allSingle:
        value = validPossibilities[current][0]
        for index in validPossibilities:
            if index != current and value in validPossibilities[index]:
                validPossibilities[index].remove(value)

indices = [i for i in validPossibilities if validPossibilities[i][0].startswith('departure')]
print('part2:', prod(n for i,n in enumerate(yourTicket) if i in indices))