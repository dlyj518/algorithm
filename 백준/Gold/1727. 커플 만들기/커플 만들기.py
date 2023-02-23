n, m = map(int, input().split())
mn = sorted(list(map(int, input().split())))
wm = sorted(list(map(int, input().split())))
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j - 1] + abs(mn[i - 1] - wm[j - 1])
        if i < j: dp[i][j] = min(dp[i][j], dp[i][j - 1])
        if i > j: dp[i][j] = min(dp[i][j], dp[i - 1][j])
print(dp[n][m])