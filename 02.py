lines = [line for line in open('in/02.txt')]

def countA(lines):
    count = 0
    for line in lines:
        parts = line.split()
        range = parts[0].split('-')
        min = int(range[0])
        max = int(range[1])
        letter = parts[1].replace(':','')
        pw = parts[2]
        pwCount = pw.count(letter)
        if (pwCount >= min and pwCount <= max):
            count += 1
    return count

def countB(lines):
    count = 0
    for line in lines:
        parts = line.split()
        range = parts[0].split('-')
        a = int(range[0]) -1
        b = int(range[1]) -1
        letter = parts[1].replace(':','')
        pw = parts[2]
        if (a > len(pw) or b > len(pw)):
            continue
        if ((pw[a] == letter or pw[b] == letter) and (pw[a] != pw[b])):
            count += 1
    return count

print(countA(lines))
print(countB(lines))