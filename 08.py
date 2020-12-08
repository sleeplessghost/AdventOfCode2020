def parseInstruction(line):
    instruction, value = line.split()
    return (instruction, int(value))

def isLooping(previousPointers): return len(previousPointers) != len(set(previousPointers))
def isCompleted(pointer, instructions): return pointer >= len(instructions)

def execute(instructions):
    accumulator, pointer, history = 0, 0, [0]
    while not (isCompleted(pointer, instructions) or isLooping(history)):
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

def executeAndReplace(originalInstructions, target, replacement):
    for i, (instr, value) in enumerate(originalInstructions):
        if instr == target:
            instructions = originalInstructions.copy()
            instructions[i] = (replacement, value)
            pointer, accumulator = execute(instructions)
            if isCompleted(pointer, instructions): return accumulator

instructions = list([parseInstruction(line) for line in open('in/08.txt')])

__, part1 = execute(instructions)
jmp = executeAndReplace(instructions, 'nop', 'jmp')
nop = executeAndReplace(instructions, 'jmp', 'nop')

print('part1:', part1)
print('part2 (jmp):', jmp)
print('part2 (nop):', nop)