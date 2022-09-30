import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    vs[x] = 1
    for a in rt[x]:
        if vs[a] == 0: dfs(a); vs[x] += vs[a]
n,r,q = map(int,input().split())
rt = [[] for _ in range(n+1)]
vs = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    rt[a].append(b)
    rt[b].append(a)
dfs(r)
for _ in range(q): print(vs[int(input())])