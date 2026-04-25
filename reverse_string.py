s = input()
words = s.split()

for i in range(len(words)-1, -1, -1):
    if i == 0:
        print(words[i], end="")
    else:
        print(words[i], end=" ")
        