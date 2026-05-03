n = int(input())
arr = list(map(int, input().split()))

curr_len = 1
max_len = 1

for i in range(n - 1):
    if arr[i+1] > arr[i]:
        curr_len += 1
    else:
        max_len = max(max_len, curr_len)
        curr_len = 1

max_len = max(max_len, curr_len)

print(max_len)