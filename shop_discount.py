n = int(input())
new = 0

if n > 10000:
    new = n - (n * 20 / 100)
elif n > 5000:
    new = n - (n * 10 / 100)
else:
    new = n

print(int(new))


# n = int(input())

# if n > 10000:
#     new = n - (n * 20 // 100)
# elif n > 5000:
#     new = n - (n * 10 // 100)
# else:
#     new = n

# print(new)
# new = n * 0.8