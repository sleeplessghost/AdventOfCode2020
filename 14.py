import re

def maskValue(value: int, mask: str):
    result = value | int(mask.replace('X', '0'), 2)
    return result & int(mask.replace('X', '1'), 2)

def getPermutations(binary: str):
    if 'X' not in binary:
        yield int(binary, 2)
    else:
        yield from getPermutations(binary.replace('X', '1', 1))
        yield from getPermutations(binary.replace('X', '0', 1))

lines = [line.strip() for line in open('in/14.txt')]

mask = ''
mem1, mem2 = {}, {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    elif line.startswith('mem'):
        address, value = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
        value = int(value)
        mem1[address] = maskValue(value, mask)
        binary = str(bin(int(address))).replace('0b','').zfill(len(mask))
        binary = ''.join([mask[i] if mask[i] != '0' else binary[i] for i in range(len(mask))])
        for addr in getPermutations(binary):
            mem2[addr] = value

print('part1:', sum(mem1.values()))
print('part2:', sum(mem2.values()))