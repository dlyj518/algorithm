n = int(input())
dp = [[0] + [1] * 9]
dp.extend([[0] * 10 for _ in range(n - 1)])

for i in range(1, n):
    for j in range(10):
        x = dp[i - 1][j - 1] if j > 0 else 0
        x += dp[i - 1][j + 1] if j < 9 else 0
        dp[i][j] = x
print(sum(dp[-1]) % 1000000000)