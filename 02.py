import re
from typing import Callable

def parse(line) -> (int, int, str, str):
    parsed = re.match("(?P<a>[0-9]+)-(?P<b>[0-9]+) (?P<letter>[a-zA-Z]): (?P<password>[a-zA-Z]+)", line)
    return (int(parsed.group('a')), int(parsed.group('b')), parsed.group('letter'), parsed.group('password'))

def countA(lines):
    count = 0
    for line in lines:
        (min, max, letter, password) = parse(line)
        pwCount = password.count(letter)
        if (pwCount >= min and pwCount <= max):
            count += 1
    return count

def countB(lines):
    count = 0
    for line in lines:
        (a, b, letter, password) = parse(line)
        (a, b) = (a - 1, b - 1)
        if (password[a] != password[b] and (password[a] == letter or password[b] == letter)):
            count += 1
    return count

lines = [line for line in open('in/02.txt')]

print('valid PW by letter count:', countA(lines))
print('valid PW by index:', countB(lines))

##################################################################################

def isValidLetterCount(min, max, letter, password):
    return min <= password.count(letter) <= max

def isValidIndex(a, b, letter, password):
    i,j = a - 1, b - 1
    return password[i] != password[j] and (password[i] == letter or password[j] == letter)

def getValidPWCount(lines, isValid: Callable):
    return sum(isValid(*parse(line)) for line in lines)

print('valid PW by letter count:', getValidPWCount(lines, isValidLetterCount))
print('valid PW by index:', getValidPWCount(lines, isValidIndex))