arr = list(map(int, input().split()))

min_val = min(arr)
max_val = max(arr)

n = max_val - min_val + 1

expected = n * (min_val + max_val) // 2
actual = sum(arr)

print(expected - actual)