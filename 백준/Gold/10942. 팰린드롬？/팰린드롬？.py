import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
m = int(input())
dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
    if i < n - 1 and ls[i] == ls[i+1]: dp[i][i+1] = 1
for c in range(2, n):
    for i in range(n - c):
        if dp[i + 1][i + c - 1]:
            if ls[i] == ls[i + c]: dp[i][i + c] = 1
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])