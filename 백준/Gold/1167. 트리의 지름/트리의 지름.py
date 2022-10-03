import sys
sys.setrecursionlimit(10**6)

def dfs(s,n=0):
    vs[s] = n
    for i in tr[s]:
        if vs[i[0]] == -1: dfs(i[0],n+i[1])


n = int(input())
tr = [[] for _ in range(n+1)]
vs = [-1]*(n+1)
for _ in range(n):
    a, *nd = map(int, input().split())
    for i in range(len(nd)//2):
        tr[a].append(nd[i*2:(i+1)*2])
dfs(1)
a = vs.index(max(vs))
vs = [-1]*(n+1)
dfs(a)
print(max(vs))