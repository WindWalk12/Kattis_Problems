cases = int(input())
countries = set({})

for i in range(cases):
    for j in range(int(input())):
        countries.add(str(input()))
    print(len(countries))
    countries.clear()