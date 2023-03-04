n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * m for _ in range(n)]
for i in range(m): dp[0][i] = ls[i][0]
for i in range(1, n):
    for j in range(m):
        p = c = 0
        for k in range(m):
            if j == k: continue
            p = max(p, dp[i - 1][k])
        dp[i][j] = max(dp[i - 1][j] + ls[j][i] // 2, p + ls[j][i])
print(max(dp[-1]))