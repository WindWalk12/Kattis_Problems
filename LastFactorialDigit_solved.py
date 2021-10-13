import math

cases = int(input())

for i in range(cases):
    number = int(input())

    number = math.factorial(number)
    number = str(number)[-1:]
    print(int(number))