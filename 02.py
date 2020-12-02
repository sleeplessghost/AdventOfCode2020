import re

def parse(line) -> (int, int, str, str):
    parsed = re.search("(?P<a>[0-9]+)-(?P<b>[0-9]+) (?P<letter>[a-zA-Z]): (?P<password>[a-zA-Z]+)", line)
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
        a -= 1
        b -= 1
        if ((password[a] == letter or password[b] == letter) and (password[a] != password[b])):
            count += 1
    return count

lines = [line for line in open('in/02.txt')]
print(countA(lines))
print(countB(lines))