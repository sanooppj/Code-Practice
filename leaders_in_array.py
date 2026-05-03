n = int(input())
arr = list(map(int, input().split()))

max_right = arr[n-1]
leaders = [max_right]

# traverse from right to left
for i in range(n-2, -1, -1):
    if arr[i] >= max_right:
        max_right = arr[i]
        leaders.append(arr[i])

# reverse to maintain original order
leaders.reverse()

# print result
for i in leaders:
    print(i, end=" ")