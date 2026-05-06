arr = list(map(int, input().split()))

s = set(arr)
max_len = 0

for num in s:
    if num - 1 not in s:   
        current = num
        length = 1

        while current + 1 in s:
            current += 1
            length += 1

        max_len = max(max_len, length)

print(max_len)