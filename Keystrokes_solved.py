letters = input()

def split(word):
    return list(word)

split(letters)
list1 = []
pos = 0
answer = ""

for i in range(len(letters)):
    if letters[i] != "L" and letters[i] != "R" and letters[i] != "B" and len(letters) == 1:
        list1.insert(pos, letters[i])
        pos = len(list1)
    elif letters[i] != "L" and letters[i] != "R" and letters[i] != "B":
        list1.insert(pos, letters[i])
        pos += 1
    elif letters[i] == "L":
        pos -= 1
    elif letters[i] == "R":
        pos += 1
    elif letters[i] == "B":
        list1.pop(pos-1)
        pos -= 1

answer = str(answer).join(list1)
print(answer)