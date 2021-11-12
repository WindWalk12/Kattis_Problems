d = [0,0,0,0,0]
for i in range(0,4):
    line = input()
    if i > 0:
        d[0] += line[0:9].count('o')
        d[1] += line[10:19].count('o')
        d[2] += line[20:29].count('o')
        d[3] += line[30:39].count('o')
        d[4] += line[40:49].count('o')
input()
output = ""
dices = [0,0,0,0,0,0]
dices[0] = sum(1 for item in d if item == 1)
dices[1] = sum(1 for item in d if item == 2)
dices[2] = sum(1 for item in d if item == 3)
dices[3] = sum(1 for item in d if item == 4)
dices[4] = sum(1 for item in d if item == 5)
dices[5] = sum(1 for item in d if item == 6)

output += str(dices[0]) + " "
output += str(dices[1] * 2) + " "
output += str(dices[2] * 3) + " "
output += str(dices[3] * 4) + " "
output += str(dices[4] * 5) + " "
output += str(dices[5] * 6) + " "

if dices[5] >= 2:
    output += str(12) + " "

elif dices[4] >= 2:
    output += str(10) + " "

elif dices[3] >= 2:
    output += str(8) + " "

elif dices[2] >= 2:
    output += str(6) + " "

elif dices[1] >= 2:
    output += str(4) + " "

elif dices[0] >= 2:
    output += str(2) + " "

else:
    output += str(0) + " "

loopBreak = False
for i in range(0,6):
    if(loopBreak):
        break
    for y in range(0,6):
        if(loopBreak):
            break
        if dices[5-i] >= 2 and dices[5-y] >= 2 and dices[5-y] != dices[5-i]:
            output += str(2 * (6-i) + 2 * (6-y)) + " "
            loopBreak = True
            break
if(not loopBreak):
    output += str(0) + " "

if dices[5] >= 3:
    output += str(18) + " "

elif dices[4] >= 3:
    output += str(15) + " "

elif dices[3] >= 3:
    output += str(12) + " "

elif dices[2] >= 3:
    output += str(9) + " "

elif dices[1] >= 3:
    output += str(6) + " "

elif dices[0] >= 3:
    output += str(3) + " "

else:
    output += str(0) + " "


if dices[5] >= 4:
    output += str(24) + " "

elif dices[4] >= 4:
    output += str(20) + " "

elif dices[3] >= 4:
    output += str(16) + " "

elif dices[2] >= 4:
    output += str(12) + " "

elif dices[1] >= 4:
    output += str(8) + " "

elif dices[0] >= 4:
    output += str(4) + " "

else:
    output += str(0) + " "

loopBreak = False
for i in range(0,6):
    if(loopBreak):
        break
    for y in range(0,6):
        if(loopBreak):
            break
        if dices[5-i] >= 3 and dices[5-y] >= 2 and dices[5-y] != dices[5-i]:
            output += str(3 * (6-i) + 2 * (6-y)) + " "
            loopBreak = True
            break
if(not loopBreak):
    output += str(0) + " "

if dices[0] >= 1 and dices[1] >= 1 and dices[2] >= 1 and dices[3] >= 1 and dices[4] >= 1:
    output += str(15) + " "
else:
    output += str(0) + " "

if dices[5] >= 1 and dices[1] >= 1 and dices[2] >= 1 and dices[3] >= 1 and dices[4] >= 1:
    output += str(20) + " "
else:
    output += str(0) + " "

if dices[0] == 5 or dices[1] == 5 or dices[2] == 5 or dices[3] == 5 or dices[4] == 5 or dices[5] == 5:
    output += str(50) + " "
else:
    output += str(0) + " "

output += str(dices[0] + dices[1] * 2 + dices[2] * 3 + dices[3] * 4 + dices[4] * 5 + dices[5] * 6)

print(output)