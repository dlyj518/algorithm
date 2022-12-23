n = int(input())
cs = [list(map(int, input().split())) for _ in range(n)]
rst = 1e6
for i in range(3):
    dp = [[1e6]*3 for _ in range(n)]
    dp[0][i] = cs[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + cs[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + cs[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + cs[j][2]
    for j in range(3):
        if i != j: rst = min(rst, dp[-1][j])
print(rst)