def parseInstruction(line):
    instruction, value = line.split()
    return (instruction, int(value))

def isLooping(previousPointers): return len(previousPointers) != len(set(previousPointers))
def isCompleted(pointer, instructions): return pointer >= len(instructions)

def execute(instructions):
    accumulator, pointer, previous = 0, 0, []
    while pointer < len(instructions):
        previous.append(pointer)
        if isLooping(previous): break

        instr, value = instructions[pointer]
        if instr == 'jmp':
            pointer += value
        elif instr == 'nop':
            pointer += 1
        elif instr == 'acc':
            pointer += 1
            accumulator += value
    return (pointer, accumulator)

def executeAndReplace(originalInstructions, target, replacement):
    totalCount = sum(1 for (instruction, value) in originalInstructions if instruction.startswith(target))
    for i in range(totalCount):
        instructions = replaceNth(originalInstructions, i, target, replacement)
        pointer, accumulator = execute(instructions)
        if isCompleted(pointer, instructions): return accumulator
    return False

def replaceNth(instructions, n, target, replacement):
    count, newList = 0, instructions.copy()
    for i in range(len(newList)):
        instr, value = newList[i]
        if instr == target:
            if count == n:
                newList[i] = (replacement, value)
                break
            else: count += 1
    return newList

instructions = list([parseInstruction(line) for line in open('in/08.txt')])

__, part1 = execute(instructions)
jmp = executeAndReplace(instructions, 'nop', 'jmp')
nop = executeAndReplace(instructions, 'jmp', 'nop')

print('part1:', part1)
print('part2 (jmp):', jmp)
print('part2 (nop):', nop)