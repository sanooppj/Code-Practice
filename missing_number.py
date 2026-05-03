n = int(input())
arr = list(map(int, input().split()))

mine = min(arr)
maxe = max(arr)

expected = (n * (mine + maxe)) // 2
actual = sum(arr)

print(expected - actual)