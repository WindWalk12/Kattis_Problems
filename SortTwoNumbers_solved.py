numbers = input()
a, b = numbers.split()
a = int(a)
b = int(b)

if b > a:
    print(str(a) + " " + str(b))
else:
    print(str(b) + " " + str(a))