import re

def passportIsValid(passport):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return (all(field in passport for field in requiredFields) and
        all(fieldIsValid(field, passport[field]) for field in requiredFields))

def fieldIsValid(name, value):
    if (name == 'byr'): return all(str.isdigit(c) for c in value) and 1920 <= int(value) <= 2002
    elif (name == 'iyr'): return all(str.isdigit(c) for c in value) and 2010 <= int(value) <= 2020
    elif (name == 'eyr'): return all(str.isdigit(c) for c in value) and 2020 <= int(value) <= 2030
    elif (name == 'hcl'): return re.match(r'^#[a-zA-Z0-9]{6}$', value) != None
    elif (name == 'ecl'): return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif (name == 'pid'): return all(str.isdigit(c) for c in value) and len(value) == 9
    elif (name == 'hgt'):
        measurement = value[-2:]
        height = value[0:-2]
        return (str.isdigit(c) for c in height) and (
            (measurement == 'cm' and 150 <= int(height) <= 193) or
            (measurement == 'in' and 59 <= int(height) <= 76))

lines = [line.strip() for line in open('in/04.txt')]

passports = []
p = {}
for line in lines:
    if line == '\n' or not line:
        passports.append(p)
        p = {}
    else:
        parts = line.split(' ')
        for part in parts:
            if part:
                x = part.split(':')
                t = x[0]
                v = x[1]
                p[t] = v
passports.append(p)

valid = 0
for p in passports:
    valid += passportIsValid(p)

print(valid)
