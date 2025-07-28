n, t = map(int, input().split())
dp = [[0] * (t + 1) for _ in range(n + 1)]
dm = [[0, 0]]
mx = 0
for i in range(n): dm.append(list(map(int, input().split())))
for i in range(1,  n + 1):
    [d, m] = dm[i]
    mx += m
    for j in range(t + 1):
        dp[i][j] = dp[i - 1][j] if j < d else max(dp[i - 1][j], dp[i - 1][j - d] + m)
print(mx - dp[-1][-1])