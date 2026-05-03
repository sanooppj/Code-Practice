arr = list(map(int, input().split()))
n = len(arr)

max_len = 0

for i in range(n):
    seen = []
    for j in range(i, n):
        if arr[j] in seen:
            break
        seen.append(arr[j])
    
    max_len = max(max_len, len(seen))

print(max_len) 