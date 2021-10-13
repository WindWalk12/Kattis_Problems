price = float(input())
lawns = int(input())
cost = 0

for i in range(lawns):
    a, b = input().split()
    a = float(a)
    b = float(b)

    cost += (a * b)

print(cost * price)