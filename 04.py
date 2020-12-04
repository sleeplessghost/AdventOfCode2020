def isValid(p):
    byr = p['byr']
    iyr = p['iyr']
    eyr = p['eyr']
    hgt =p['hgt']
    hcl = p['hcl']
    ecl =  p['ecl']
    pid = p['pid']
    bval = byr != None and len(byr) == 4 and 1920 <= int(byr) <= 2002
    ival = iyr != None and len(iyr) == 4 and 2010 <= int(iyr) <= 2020
    evl = eyr != None and len(eyr) == 4 and 2020 <= int(eyr) <= 2030
    h0 = hgt[-2:] if hgt != None else None
    h1 = hgt[0:-2] if hgt != None else None
    hval = hgt != None and ((h0 == 'cm' and 150 <= int(h1) <= 193) or (h0 == 'in' and 59 <= int(h1) <= 76))
    hc0 = hcl[1:] if hcl != None else None
    hcval = hcl != None and (hcl[0] == '#' and len(hc0) == 6 and all(str.isalpha(c) or str.isdigit(c) for c in hc0))
    ecval = ecl != None and (ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth')
    pval = pid != None and (len(pid) == 9 and all(str.isdigit(c) for c in pid))
    return bval and ival and evl and hval and hcval and ecval and pval

lines = [line.strip() for line in open('in/04.txt')]

passports = []
p = {
    'byr': None,
    'iyr': None,
    'eyr': None,
    'hgt': None,
    'hcl': None,
    'ecl': None,
    'pid': None,
    'cid': None,
}
for line in lines:
    if line == '\n' or not line:
        passports.append(p)
        p = {
            'byr': None,
            'iyr': None,
            'eyr': None,
            'hgt': None,
            'hcl': None,
            'ecl': None,
            'pid': None,
            'cid': None,
        }
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
    valid += isValid(p)

print(valid)
