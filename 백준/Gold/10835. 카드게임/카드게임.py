n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            if a[i] > b[j]:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b[j])
m1 = max(dp[-1])
m2 = max(dpi[-1] for dpi in dp)
print(max(m1, m2))