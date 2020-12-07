import re

def makeDictionary(lines):
    dictionary = {}
    for line in lines:
        colour = re.search(r'(.+) bags contain', line)[1]
        dictionary[colour] = {}
        for amount, innerColour in re.findall(r'(\d) (\w+ \w+)', line):
            dictionary[colour][innerColour] = int(amount)
    return dictionary

def contains(colour, dictionary, results, target):
    if colour not in results:
        containsTarget = target in dictionary[colour]
        results[colour] = containsTarget or any(
            contains(innerColour, dictionary, results, target) 
            for innerColour in dictionary[colour])
    return results[colour]

def countInside(colour, dictionary, counts):
    if colour not in counts:
        counts[colour] = sum(
            amount + amount * countInside(innerColour, dictionary, counts) 
            for innerColour, amount in dictionary[colour].items())
    return counts[colour]

dictionary = makeDictionary(open('in/07.txt'))
containsDict = {}
countsDict = {}
target = 'shiny gold'

part1 = sum(
    contains(colour, dictionary, containsDict, target)
    for colour in dictionary if colour != target)
part2 = countInside(target, dictionary, countsDict)

print('part1:', part1)
print('part2:', part2)