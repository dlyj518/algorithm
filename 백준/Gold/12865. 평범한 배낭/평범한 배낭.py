n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(2)]
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(w, k+1):
        dp[1][i] = max(dp[0][i], v+dp[0][i-w])
    dp[0] = dp[1][:]
print(dp[1][k])
