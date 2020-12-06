import re
from typing import Callable

def parse(line) -> (int, int, str, str):
    parsed = re.match(r"(\d+)-(\d+) (\S): (\S+)", line)
    a, b, letter, password = parsed.groups()
    return (int(a), int(b), letter, password)

def isValidLetterCount(min, max, letter, password):
    return min <= password.count(letter) <= max

def isValidIndex(a, b, letter, password):
    i, j = a - 1, b - 1
    return (password[i] == letter) != (password[j] == letter)

def getValidPWCount(passwords, isValid: Callable):
    return sum(isValid(*p) for p in passwords)

passwords = [parse(line) for line in open('in/02.txt')]
print('part1:', getValidPWCount(passwords, isValidLetterCount))
print('part2:', getValidPWCount(passwords, isValidIndex))