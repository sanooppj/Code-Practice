s = input()
n = len(s)

max_len = 0

for i in range(n):
    seen = ""
    
    for j in range(i, n):
        if s[j] in seen:
            break
        seen += s[j]
    
    if len(seen) > max_len:
        max_len = len(seen)

print(max_len)