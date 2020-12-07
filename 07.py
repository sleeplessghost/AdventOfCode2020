import re

def makeDictionary(lines):
    dictionary = {}
    for line in lines:
        colour = re.search(r'(.+) bags contain', line)[1]
        dictionary[colour] = {}
        for amount, innerColour in re.findall(r'(\d) (\w+ \w+)', line):
            dictionary[colour][innerColour] = int(amount)
    return dictionary

def contains(name, dictionary, results, target):
    if name not in results:
        containsTarget = target in dictionary[name].keys()
        results[name] = containsTarget or any(
            contains(innerColour, dictionary, results, target) 
            for innerColour in dictionary[name].keys())
    return results[name]

def countInside(name, dictionary, counts):
    if name not in counts:
        counts[name] = sum(
            amount + amount * countInside(colour, dictionary, counts) 
            for colour, amount in dictionary[name].items())
    return counts[name]

dictionary = makeDictionary(open('in/07.txt'))
containsDict = {}
countsDict = {}
target = 'shiny gold'

part1 = sum(
    contains(name, dictionary, containsDict, target)
    for name in dictionary.keys() if name != target)
part2 = countInside(target, dictionary, countsDict)

print('part1:', part1)
print('part2:', part2)