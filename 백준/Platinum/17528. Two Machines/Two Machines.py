import sys
input = sys.stdin.readline

n = int(input())
dp = [100000] * (250 * 250 + 1)
dp[0] = 0
sa = 0
for _ in range(n):
    a, b = map(int, input().split())
    sa += a
    for i in range(len(dp) - 1, a - 1, -1):
        dp[i] = min(dp[i], dp[i - a] + b)
ans = 1e6
for i in range(len(dp)): ans = min(ans, max(sa - i, dp[i]))
print(ans)