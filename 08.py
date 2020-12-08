accum = 0

instructions = open('in/08.txt').read().splitlines()
accum = 0

i = 0
prevInstr = []
while i < len(instructions):
    inst = instructions[i]
    parts = inst.split()
    do, num = parts[0], int(parts[1])
    print(do, num)
    if (i in prevInstr): break
    prevInstr.append(i)

    if (do == 'jmp'): i += num
    else:
        if (do == 'acc'): accum += num
        #if (do == 'nop'): 
        i += 1

print(accum)