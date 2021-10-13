import math

cases = int(input())
appears = None

for i in range(cases):
    a = input().split()
    year = int(a[0])
    pair1 = int(a[1])
    pair2 = int(a[2])
    next = pair1 * pair2 // math.gcd(pair1, pair2) + year
    if appears is None or next < appears:
        appears = next

print(appears)