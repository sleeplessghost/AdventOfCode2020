import re

def getPermutations(binary):
    if 'X' not in binary:
        yield int(binary, 2)
    else:
        yield from getPermutations(binary.replace('X', '1', 1))
        yield from getPermutations(binary.replace('X', '0', 1))

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
        binary = ''.join(binary)
        for addr in getPermutations(binary):
            mem[addr] = int(value)

print('part2:', sum(mem.values()))