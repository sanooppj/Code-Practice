N = 4
values = [1, 2, 3, 4]
end = 3
R = len(values)
dp = [[0]*R for _ in range(N)]
dp[0][0] = 1
for i in range(1, N):
    for j in range(R):
        for k in range(R):
            if values[j] != values[k]:
                if i == N-1 and values[j] != end:
                    continue
                dp[i][j] += dp[i-1][k]
print(sum(dp[N-1][j] for j in range(R) if values[j] == end))