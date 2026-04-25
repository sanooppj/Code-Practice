s = input()

count = {}
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

found = False
for ch in s:
    if count[ch] == 1:
        print(ch)
        found = True
        break

if not found:
    print(-1)