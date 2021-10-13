a, b = input().split()
a = str(a)[::-1]
b = str(b)[::-1]

if a > b:
    print(int(a))
else:
    print(int(b))