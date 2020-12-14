import re
from collections import defaultdict

def getAllValsFor(i, masked, arr):
    if i >= len(masked):
        arr.append(''.join(masked))
    elif masked[i] == 'X':
        zero = masked.copy()
        zero[i] = '0'
        getAllValsFor(i + 1, zero, arr)
        one = masked.copy()
        one[i] = '1'
        getAllValsFor(i + 1, one, arr)
    else:
        getAllValsFor(i + 1, masked, arr)

lines = [line.strip() for line in open('in/14.txt')]

mask = ''
mem = defaultdict(int)
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
mem = defaultdict(int)
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
        perms = []
        getAllValsFor(0, binary, perms)
        for addr in perms:
            converted = int(addr, 2)
            mem[addr] = int(value)

print('part2:', sum(mem.values()))