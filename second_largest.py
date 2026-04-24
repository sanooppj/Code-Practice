n = int(input())
arr = list(map(int, input().split()))

first = -1
second = -1

for i in range(n):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second and arr[i] != first:
        second = arr[i]

print(second)