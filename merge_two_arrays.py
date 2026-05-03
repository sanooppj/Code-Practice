arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []

for num in arr1 + arr2:
    if num not in result:
        result.append(num)

print(result)



# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

# result = list(set(arr1 + arr2))
# print(result)