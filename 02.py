import re

def parse(line) -> (int, int, str, str):
    parsed = re.match(r"(\d+)-(\d+) (\S): (\S+)", line)
    a, b, letter, password = parsed.groups()
    return (int(a), int(b), letter, password)

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