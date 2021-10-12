runtime = int(input())

a = input().split()
b = input().split()
d = list(set(a) - set(b))
print(int(d[0]))