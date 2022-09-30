def dfs(x):
    global ls
    vsd[x] = 1
    ls.append(x)
    for a in sorted(rd[x]):
        if vsd[a] == 0 : dfs(a)
    return ls

def bfs(x):
    ls = [x]
    vsb[x] = 1
    q = [x]
    while q:
        n = q.pop(0)
        for a in sorted(rd[n]):
            if vsb[a] == 0:
                ls.append(a)
                vsb[a] = 1
                q.append(a)
    return ls

n,m,v = map(int,input().split())
rd = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    rd[a].append(b)
    rd[b].append(a)
vsd, vsb = [0]*(n+1), [0]*(n+1)
ls = []
rsd = dfs(v)
rsb = bfs(v)
print(*rsd)
print(*rsb)