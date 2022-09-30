def bfs(x,g):
    if x == g: return 0
    vs = [0]*(n+1)
    vs[x] = 1
    q = [(x,1)]
    while q:
        p,c = q.pop(0)
        for a in frd[p]:
            if a == g: return c
            if vs[a] == 0:
                vs[a] = 1
                q.append((a,c+1))

n,m = map(int,input().split())
frd = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    frd[a].append(b)
    frd[b].append(a)
mn,rst = n**2, 0
for i in range(n):
    sm = 0
    for j in range(n):
        sm += bfs(i+1,j+1)
    if sm < mn: mn, rst = sm, i+1
print(rst)