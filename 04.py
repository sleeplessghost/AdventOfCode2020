import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def parsePassport(passportInput):
    return dict(re.findall(r'(\S+):(\S+)', passportInput))

def hasRequiredFields(passport):
    return all(field in passport for field in REQUIRED_FIELDS)

def isValid(passport):
    return (hasRequiredFields(passport) and
        all(fieldIsValid(field, passport[field]) for field in REQUIRED_FIELDS))

def fieldIsValid(name, value):
    if (name == 'byr'): return value.isdigit() and 1920 <= int(value) <= 2002
    elif (name == 'iyr'): return value.isdigit() and 2010 <= int(value) <= 2020
    elif (name == 'eyr'): return value.isdigit() and 2020 <= int(value) <= 2030
    elif (name == 'hcl'): return re.match(r'^#[a-fA-F0-9]{6}$', value) is not None
    elif (name == 'ecl'): return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif (name == 'pid'): return value.isdigit() and len(value) == 9
    elif (name == 'hgt'):
        height, units = value[:-2], value[-2:]
        return height.isdigit() and (
            (units == 'cm' and 150 <= int(height) <= 193) or
            (units == 'in' and 59 <= int(height) <= 76))

text = open('in/04.txt').read()
passports = [parsePassport(p) for p in text.split('\n\n')]

print('part1:', sum(hasRequiredFields(p) for p in passports))
print('part2:', sum(isValid(p) for p in passports))