aShots, bShots = input().split()
aShots = int(aShots)
bShots = int(bShots)

aAlcohol = 0
bAlcohol = 0

for i in range(aShots):
    a, b = input().split()
    a = int(a)
    b = int(b)
    aAlcohol = aAlcohol + (a*b)

for i in range(bShots):
    a, b = input().split()
    a = int(a)
    b = int(b)
    bAlcohol = bAlcohol + (a * b)

if (aAlcohol == bAlcohol):
    print("same")
else:
    print("different")

