n = int(input())
arr = list(map(int, input().split()))

first = float('-inf')
second = float('-inf')
third = float('-inf')

for i in range(n):
    if arr[i] > first:
        third = second
        second = first
        first = arr[i]
    elif arr[i] > second and arr[i] != first:
        third = second
        second = arr[i]
    elif arr[i] > third and arr[i] != second and arr[i] != first:
        third = arr[i]

if third == float('-inf'):
    print(-1)
else:
    print(third)