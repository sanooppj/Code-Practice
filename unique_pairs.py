# Read input
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

count = 0

# Count pairs
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == k:
            count += 1

# Print result
print(count)