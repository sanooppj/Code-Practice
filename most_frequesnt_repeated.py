n = int(input())
arr = list(map(int, input().split()))

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max_count = 0
result = float("inf")  
for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        result = key
    elif freq[key] == max_count:
        if key < result:
            result = key

print(result)