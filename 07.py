import re

def makeDictionary(lines):
    dictionary = {}
    for line in lines:
        colour = re.search(r'(.+) bags contain', line)[1]
        dictionary[colour] = {}
        for amount, innerColour in re.findall(r'(\d) (\w+ \w+)', line):
            dictionary[colour][innerColour] = int(amount)
    return dictionary

def contains(current, dictionary, results, target):
    if current in results: return results[current]
    if target in dictionary[current].keys():
        results[current] = True
        return True
    inside = any(
        contains(innerColour, dictionary, results, target) 
        for innerColour in dictionary[current].keys())
    results[current] = inside
    return inside

def countInside(name, dictionary):
    return sum(
        amount + (amount * countInside(colour, dictionary))
        for colour, amount in dictionary[name].items())

dictionary = makeDictionary(open('in/07.txt'))
containsDict = {}

part1 = sum(
    contains(name, dictionary, containsDict, 'shiny gold')
    for name in dictionary.keys() if name != 'shiny gold')
part2 = countInside('shiny gold', dictionary)

print('part1:', part1)
print('part2:', part2)