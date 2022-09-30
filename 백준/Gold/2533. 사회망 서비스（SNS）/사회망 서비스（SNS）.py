import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    vs[x] = 1
    rst[x][1] = 1
    for a in chd[x]:
        if not vs[a]:
            dfs(a)
            rst[x][0] += rst[a][1]
            rst[x][1] += min(rst[a])

n = int(input())
vs = [0]*(n+1)
chd = [[] for _ in range(n+1)]
rst = [[0,0] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    chd[a].append(b)
    chd[b].append(a)
dfs(1)
print(min(rst[1]))