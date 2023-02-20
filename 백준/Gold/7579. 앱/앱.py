n, m = map(int, input().split())
an = list(map(int, input().split()))
cn = list(map(int, input().split()))
c = sum(cn)
dp = [[0] * (c + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(c + 1):
        dp[i + 1][j] = dp[i][j] if cn[i] > j else max(dp[i][j], dp[i][j - cn[i]] + an[i])
        if i == n - 1 and dp[i + 1][j] >= m: print(j); break