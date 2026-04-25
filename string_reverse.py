s = input()

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("YES")
else:
    print("NO")