
def parseLine(line):
    ingredients, allergens = line.split(' (')
    ingredients = ingredients.split(' ')
    allergens = allergens.replace('contains','').replace(')','').replace(' ','').split(',')
    return ingredients, allergens

parsed = [parseLine(line.strip()) for line in open('in/21.txt')]
dictionary = {}
for ingredients, allergens in parsed:
    for allerg in allergens:
        if allerg not in dictionary: dictionary[allerg] = []
        dictionary[allerg].append(set(ingredients))

allThems = []
uniqueIngrs = {}
for allergen in dictionary:
    combined = dictionary[allergen][0]
    for nx in range(1, len(dictionary[allergen])):
        combined = combined.intersection(dictionary[allergen][nx])
    allThems.append(combined)
    uniqueIngrs[allergen] = combined
unique = allThems[0]
for i in range(1, len(allThems)):
    unique = unique.union(allThems[i])

allIngredients = []
for ingredients, allergens in parsed:
    for ingr in ingredients:
        allIngredients.append(ingr)
allIngredients = set(allIngredients)

noAllerg = [x for x in allIngredients if x not in unique]
count = 0
for ingredients, __ in parsed:
    matched = [x for x in ingredients if x in noAllerg]
    count += len(matched)
print('part1:', count)

while any(len(ingrs) != 1 for ingrs in uniqueIngrs.values()):
    for allergen in uniqueIngrs:
        ingredients = uniqueIngrs[allergen]
        if len(ingredients) == 1:
            v = next(iter(ingredients))
            for a in uniqueIngrs:
                if a != allergen and v in uniqueIngrs[a]:
                    uniqueIngrs[a].remove(v)

sort = sorted([*uniqueIngrs])
values = [''.join(uniqueIngrs[key]) for key in sort]
print('part2:', ','.join(values))