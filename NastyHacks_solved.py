cases = int(input())

for i in range(cases):
    a, b, c = input().split()

    a = int(a)
    b = int(b)
    c = int(c)

    if (b-c) > a:
        print("advertise")
    elif (b-c) < a:
        print("do not advertise")
    elif (b - c) == a:
        print("does not matter")