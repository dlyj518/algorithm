import sys
sys.setrecursionlimit(10**6)

def dfs(s,n=0):
    vs[s] = n
    for i in tr[s]:
        if vs[i[0]] == -1: dfs(i[0],n+i[1])


n = int(input())
tr = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, g = map(int, input().split())
    tr[p].append([c,g])
    tr[c].append([p,g])
rst = 0
vs = [-1]*(n+1)
dfs(1)
x1 = vs.index(max(vs))
vs = [-1]*(n+1)
dfs(x1)
print(max(vs))