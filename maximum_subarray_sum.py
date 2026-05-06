# n = int(input())
# arr = list(map(int, input().split()))

# max_sum = arr[0]
# current_sum = arr[0]

# for i in range(1, n):
#     current_sum = max(arr[i], current_sum + arr[i])
#     max_sum = max(max_sum, current_sum)

# print(max_sum)




arr = list(map(int, input().split()))
K = int(input())

n = len(arr)

# find sum of first K elements
current_sum = 0
for i in range(K):
    current_sum += arr[i]

max_sum = current_sum

# slide the window
for i in range(K, n):
    current_sum = (current_sum + arr[i]) - arr[i-K]
    
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)