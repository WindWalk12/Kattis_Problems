cases = int(input())

for i in range(cases):
    a, b = input().split()
    a = int(a)
    b = float(b)

    bpm = (60*a) / b
    abpm = 60 / b

    min_abpm = bpm - abpm
    max_abpm = bpm + abpm

    print(str(min_abpm) + " " + str(bpm) + " " + str(max_abpm))