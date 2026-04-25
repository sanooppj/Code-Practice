n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)

# n = int(input())
# arr = list(map(int, input().split()))

# current_sum = arr[0]
# max_sum = arr[0]

# start = 0
# end = 0
# temp_start = 0

# for i in range(1, n):
#     if arr[i] > current_sum + arr[i]:
#         current_sum = arr[i]
#         temp_start = i
#     else:
#         current_sum = current_sum + arr[i]

#     if current_sum > max_sum:
#         max_sum = current_sum
#         start = temp_start
#         end = i

# # Print subarray
# for i in range(start, end + 1):
#     print(arr[i], end=" ")