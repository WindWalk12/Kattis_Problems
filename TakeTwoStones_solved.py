stones = int(input())
winner = ""
player = "Alice"

while stones >= 1:
    if stones == 1:
        winner = "Alice"
        break
    elif stones == 2:
        winner = "Bob"
        break
    elif player == "Alice":
        stones -= 2
    elif player == "Bob":
        stones -= 2

print(winner)