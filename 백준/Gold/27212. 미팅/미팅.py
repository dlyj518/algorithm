n, m, c = map(int, input().split())
w = [[0] * (m + 1)]
for _ in range(c):
    w.append([0] + list(map(int, input().split())))
nn = list(map(int, input().split()))
mm = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + w[nn[i - 1]][mm[j - 1]], dp[i][j - 1], dp[i - 1][j])
print(dp[-1][-1])