import re

def getAllValsFor(i, masked):
    if i >= len(masked):
        yield ''.join(masked)
    elif masked[i] == 'X':
        zero = masked.copy()
        zero[i] = '0'
        one = masked.copy()
        one[i] = '1'
        for s in getAllValsFor(i + 1, zero): yield s
        for s in getAllValsFor(i + 1, one): yield s
    else:
        for s in getAllValsFor(i + 1, masked): yield s

lines = [line.strip() for line in open('in/14.txt')]

mask = ''
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    elif line.startswith('mem'):
        address, value = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
        binary = str(bin(int(value))).replace('0b','')
        lengthDiff = len(mask) - len(binary)
        binary = list(lengthDiff * '0' + binary)
        for i, c in enumerate(mask):
            if c != 'X':
                binary[i] = c
        mem[address] = int(''.join(binary), 2)

print('part1:', sum(mem.values()))

mask = ''
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    elif line.startswith('mem'):
        address, value = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
        binary = str(bin(int(address))).replace('0b','')
        lengthDiff = len(mask) - len(binary)
        binary = list(lengthDiff * '0' + binary)
        for i, c in enumerate(mask):
            if c == 'X' or c == '1':
                binary[i] = c
        for addr in getAllValsFor(0, binary):
            converted = int(addr, 2)
            mem[addr] = int(value)

print('part2:', sum(mem.values()))