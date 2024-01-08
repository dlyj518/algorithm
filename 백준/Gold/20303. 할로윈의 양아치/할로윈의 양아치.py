import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    vs[x] = 0
    w, c = 1, cn[x]
    for i in tr[x]:
        if vs[i]: [a, b] = dfs(i); w += a; c += b
    return [w, c]

n, m, k = map(int, input().split())
cn = [0] + list(map(int, input().split()))
tr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    tr[a].append(b); tr[b].append(a)

vs = [1] * (n + 1)
dp = [0] * k
for i in range(1, n + 1):
    if vs[i]:
        a, b = dfs(i)
        for i in range(k - 1, a - 1, -1): dp[i] = max(dp[i], dp[i - a] + b)
print(dp[-1])