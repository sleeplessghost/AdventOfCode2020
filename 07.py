
def canContainGold(name, dictionary, resultDict):
    if name == 'shiny gold': return True
    if name == 'no other bags': return False

    if name in resultDict: return resultDict[name]

    subtypes = dictionary[name].keys()
    result = any(canContainGold(containedType, dictionary, resultDict) for containedType in subtypes)
    resultDict[name] = result
    return result

def countSubBags(name, dictionary):
    subdict = dictionary[name]    

    count = 1
    for key in subdict.keys():
        count += subdict[key] * countSubBags(key, dictionary)
    
    return count

dictionary = {}
resultDict = {}
countDict = {}
lines = [line.strip() for line in open('in/07.txt')]

for line in lines:
    parts = line.split(' bags contain ')
    typ = parts[0]
    ls = parts[1].replace('.','')
    thisdict = {}
    if typ in dictionary: thisdict = dictionary[typ]
    #if type == 'shiny gold': continue
    
    if ls != 'no other bags':
        for x in ls.split(', '):
            sp = x.split(' ', 1)
            num = int(sp[0])
            name = sp[1].replace(' bags','').replace(' bag','')

            thisdict[name] = num
    
    dictionary[typ] = thisdict

#test = sum(canContainGold(name, dictionary, resultDict) for name in dictionary.keys())
#print(sum(resultDict.values()))
# print(dictionary)
# print(resultDict)

print(countSubBags('shiny gold', dictionary) - 1)
# for key in dictionary.keys():
#     print(key, countSubBags(key, dictionary))