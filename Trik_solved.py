flips = input()
ball = 1


def split(word):
    return list(word)


flips = split(flips)


for i in range(len(flips)):
    if flips[i] == "A" and ball == 1:
        ball = 2
    elif flips[i] == "A" and ball == 2:
        ball = 1
    elif flips[i] == "C" and ball == 1:
        ball = 3
    elif flips[i] == "C" and ball == 3:
        ball = 1
    elif flips[i] == "B" and ball == 2:
        ball = 3
    elif flips[i] == "B" and ball == 3:
        ball = 2

print(ball)