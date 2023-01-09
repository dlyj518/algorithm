import sys
input = sys.stdin.readline

def dfs(x, r):
    if dp[x][r]: return dp[x][r]
    if r == ns - 1:
        if mt[x][0]: return mt[x][0]
        return 1e9
    mn = 1e9
    for i in range(1, n):
        if not mt[x][i]: continue
        if r & (1 << i - 1): continue
        ds = mt[x][i] + dfs(i, r | (1 << i - 1))
        mn = min(mn, ds)
    dp[x][r] = mn
    return mn

n = int(input())
mt = [list(map(int, input().split())) for _ in range(n)]
ns = 1 << n - 1
dp = [[0] * ns for _ in range(n)]

print(dfs(0, 0))