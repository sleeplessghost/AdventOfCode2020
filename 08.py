accum = 0

instructions = open('in/08.txt').read().splitlines()
accum = 0

# i = 0
# prevInstr = []
# while i < len(instructions):
#     inst = instructions[i]
#     parts = inst.split()
#     do, num = parts[0], int(parts[1])
#     print(do, num)
#     if (i in prevInstr): break
#     prevInstr.append(i)

#     if (do == 'jmp'): i += num
#     else:
#         if (do == 'acc'): accum += num
#         #if (do == 'nop'): 
#         i += 1

# print(accum)

totalNops = sum(1 for x in instructions if x.startswith('nop'))
totalJmps = sum(1 for x in instructions if x.startswith('jmp'))

replaced = False
success = False
prevInstr = []
for i in range(totalJmps):
    print()
    print('replace', i)
    copy = list(instructions).copy()
    replaced = False
    currCount = 0
    for j in range(len(copy)):
        if copy[j].startswith('jmp'):
            if currCount == i:
                copy[j] = copy[j].replace('jmp', 'nop')
                replaced = True
            currCount += 1

    print(instructions)
    print(copy)
    if not replaced: break

    prevInstr = []
    accum = 0
    sub = 0
    while sub < len(copy):
        inst = copy[sub]
        parts = inst.split()
        do, num = parts[0], int(parts[1])
        print(do, num)

        prevInstr.append(sub)
        if len(prevInstr) != len(set(prevInstr)): break        

        if (do == 'jmp'): sub += num
        else:
            if (do == 'acc'): accum += num
            #if (do == 'nop'): 
            sub += 1
    
    if len(prevInstr) == len(set(prevInstr)):
        success = True
        break

print()
print(success, accum)