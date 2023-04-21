n, l, r = map(int, input().split())
dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1][1] = 1
for k in range(2, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[k][i][j] = (dp[k - 1][i - 1][j] + dp[k - 1][i][j - 1] + dp[k - 1][i][j] * (k - 2)) % 1000000007
print(dp[n][l][r])