import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def parsePassport(passportInput):
    return dict(re.findall(r'(\S+):(\S+)', passportInput))

def passportHasRequiredFields(passport):
    return all(field in passport for field in REQUIRED_FIELDS)

def passportIsValid(passport):
    return (passportHasRequiredFields(passport) and
        all(fieldIsValid(field, passport[field]) for field in REQUIRED_FIELDS))

def fieldIsValid(name, value):
    if (name == 'byr'): return str.isdigit(value) and 1920 <= int(value) <= 2002
    elif (name == 'iyr'): return str.isdigit(value) and 2010 <= int(value) <= 2020
    elif (name == 'eyr'): return str.isdigit(value) and 2020 <= int(value) <= 2030
    elif (name == 'hcl'): return re.match(r'^#[a-zA-Z0-9]{6}$', value) is not None
    elif (name == 'ecl'): return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif (name == 'pid'): return str.isdigit(value) and len(value) == 9
    elif (name == 'hgt'):
        height, units = value[:-2], value[-2:]
        return str.isdigit(height) and (
            (units == 'cm' and 150 <= int(height) <= 193) or
            (units == 'in' and 59 <= int(height) <= 76))

input = open('in/04.txt').read()
passports = [parsePassport(p) for p in input.split('\n\n')]

hasRequired = sum(passportHasRequiredFields(p) for p in passports)
fullyValid = sum(passportIsValid(p) for p in passports)

print('part1:', hasRequired)
print('part2:', fullyValid)