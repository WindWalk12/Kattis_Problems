letters = input()

def split(word):
    return list(word)

split(letters)
answer = []
for i in range(len(letters)):
    if letters[i] != "L" or letters[i] != "R" or letters[i] != "B":
        answer.append(letters[i])
    elif letters[i] == "L":
