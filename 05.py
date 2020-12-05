import re


lines = [line.strip() for line in open('in/05.txt') if line]

max = 0
seats = []
for line in lines:
    fb, rl = line[:-3], line[-3:]
    binary = '0b' + fb.replace('B','1').replace('F','0')
    row = int(binary, 2)
    rlbin = '0b' + rl.replace('R', '1').replace('L', '0')
    col = int(rlbin, 2)
    seat = (row * 8) + col
    if (seat > max): max = seat
    seats.append(seat)

print(max)

possibleseats = []
for row in range(0, 128):
    for col in range(0, 8):
        possibleseats.append((row * 8) + col)

ls = list(seats)
for s in possibleseats:
    if s not in ls and s-1 in ls and s+1 in ls:
        print(s)