javelins = int(input())
length = 0

for i in range(javelins):
    a = int(input())
    length += a

print(length - (javelins - 1))