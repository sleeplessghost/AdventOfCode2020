def parseInstruction(line):
    instruction, value = line.split()
    return (instruction, int(value))

def isLooping(pointerHistory): return len(pointerHistory) != len(set(pointerHistory))
def isCompleted(pointer, instructions): return pointer >= len(instructions)

def execute(instructions):
    accumulator, pointer, history = 0, 0, [0]
    while not (isLooping(history) or isCompleted(pointer, instructions)):
        instr, value = instructions[pointer]
        if instr == 'jmp':
            pointer += value
        elif instr == 'nop':
            pointer += 1
        elif instr == 'acc':
            pointer += 1
            accumulator += value
        history.append(pointer)
    return (pointer, accumulator)

def executeAndReplace(instructions, target, replacement):
    for i, (instr, value) in enumerate(instructions):
        if instr == target:
            instructions[i] = (replacement, value)
            pointer, accumulator = execute(instructions)
            instructions[i] = (instr, value)
            if isCompleted(pointer, instructions): return accumulator

instructions = [parseInstruction(line) for line in open('in/08.txt')]

__, part1 = execute(instructions)
jmp = executeAndReplace(instructions, 'nop', 'jmp')
nop = executeAndReplace(instructions, 'jmp', 'nop')

print('part1:', part1)
print('part2 (jmp):', jmp)
print('part2 (nop):', nop)