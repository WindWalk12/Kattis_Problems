numOfBottles = int(input())
desiredOpened = int(input())
opener = numOfBottles
opened = 0
wontWork = True

if numOfBottles == desiredOpened and wontWork:
    print("impossible")
    wontWork = False

for i in range(numOfBottles):
    while numOfBottles >= 2 and opened < desiredOpened and wontWork:
        print("open " + str(i+1) + " using " + str(opener))
        i = i + 1
        opened = opened + 1
        numOfBottles = numOfBottles - 1
