n = int(input())
m = int(1e9)
dp = [[[0] * 1024 for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10): dp[1][i][1 << i] = 1
for i in range(n):
    for j in range(10):
        for k in range(1024):
            if j < 9:
                l = k | (1 << (j + 1))
                dp[(i + 1)][j + 1][l] += dp[i][j][k]
                dp[(i + 1)][j + 1][l] %= m

            if j > 0:
                l = k | (1 << (j - 1))
                dp[(i + 1)][j - 1][l] += dp[i][j][k]
                dp[(i + 1)][j - 1][l] %= m
print(sum(dp[-1][i][-1] for i in range(10)) % m)