n = int(input())
num = list(map(int, input().split()))

new = []
zero_count = 0

for i in num:
    if i == 0:
        zero_count += 1
    else:
        new.append(i)

for i in range(zero_count):
    new.append(0)

for i in new:
    print(i, end=" ")