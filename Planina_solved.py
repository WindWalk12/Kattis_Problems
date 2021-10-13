sides = 2

for i in range(int(input())):
    sides += sides - 1

print(sides**2)