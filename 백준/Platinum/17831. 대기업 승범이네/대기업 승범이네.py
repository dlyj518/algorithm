import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    vs[x] = 0
    for i in ch[x]:
        if vs[i]: dfs(i)
    for i in ch[x]: dp[x][1] += dp[i][0]
    dp[x][0] = dp[x][1]
    for i in ch[x]: dp[x][0] = max(dp[x][0], dp[x][1] - dp[i][0] + sr[x] * sr[i] + dp[i][1])
    

n = int(input())
pr = list(map(int, input().split()))
sr = [0] + list(map(int, input().split()))
ch = [[] for _ in range(n + 1)]
vs = [1] * (n + 1)
dp = [[0, 0] for _ in range(n + 1)]
for i in range(n - 1): ch[pr[i]].append(i + 2)
dfs(1)
print(dp[1][0])