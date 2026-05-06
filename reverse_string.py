s = input()

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("YES")
else:
    print("NO")





def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

s = input()
print(reverse_string(s))





s = input()

stack = []

for ch in s:
    stack.append(ch)

rev = ""

while stack:
    rev += stack.pop()

print(rev)





s = input()

lst = list(s)
lst.reverse()

rev = "".join(lst)

print(rev)






s = input()

i = len(s) - 1
rev = ""

while i >= 0:
    rev += s[i]
    i -= 1

print(rev)





s = input()

rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print(rev)






s = input()

rev = "".join(reversed(s))

print(rev)





s = input()

rev = s[::-1]

print(rev)