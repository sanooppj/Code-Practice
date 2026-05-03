arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []

for num in arr1:
    if num in arr2 and num not in result:
        result.append(num)

print(result)