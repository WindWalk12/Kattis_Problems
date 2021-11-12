numOfBeerCans = int(input())
width = 66
heights = input().split()
done = False
for i in range(len(heights)):
    heights[i] = int(heights[i])

for i in range(numOfBeerCans):
    highest = 0
    if int(heights[i]) > highest:
        highest = heights[i]
        print(highest)

for i in range(2, numOfBeerCans):
    if (heights[i-2]) + heights[i-1] < heights[i]:
        print("no")
