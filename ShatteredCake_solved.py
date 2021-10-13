width = int(input())
cakes = int(input())

area = 0

for i in range(cakes):
    a, b = input().split()

    a = int(a)
    b = int(b)

    area += (a * b)

print(int(area/width))
