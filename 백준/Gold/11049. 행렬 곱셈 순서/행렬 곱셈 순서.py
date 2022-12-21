import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
for _ in range(n-1):
    a, b = map(int, input().split())
    m.append(b)
dp = [[0]*n for _ in range(n)]
for i in range(1, n):
    for j in range(n-i):
        k = j + i
        dp[j][k] = 2**32
        for l in range(j, k):
            dp[j][k] = min(dp[j][k], dp[j][l] + dp[l+1][k] + m[j] * m[l+1] * m[k+1])
print(dp[0][-1])