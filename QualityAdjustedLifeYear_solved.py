number_of_persons = int(input())
q = 0

for i in range(number_of_persons):
    a, b = map(float, input().split())
    q += (a*b)

print(q)
