numbers = int(input())
res = 0

for i in range(numbers):
    a = int(input())
    b = str(a)[-1:]
    a = str(a)[:-1]
    res += (pow(int(a),int(b)))

print(res)