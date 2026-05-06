arr = list(map(int, input().split()))
K = int(input())

n = len(arr)

left = 0
current_sum = 0
min_len = n + 1

for right in range(n):

    current_sum += arr[right]

    while current_sum >= K:

        length = right - left + 1

        if length < min_len:
            min_len = length

        current_sum -= arr[left]
        left += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)