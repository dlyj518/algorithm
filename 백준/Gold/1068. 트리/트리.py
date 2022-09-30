def dfs(x):
    global cnt
    if vs[x] == 1: return
    vs[x] = 1
    chk = 1
    for a in chd[x]:
        if not vs[a]: chk = 0; dfs(a)
    if chk == 1: cnt += 1

n = int(input())
par = list(map(int, input().split()))
vs = [0]*n
chd = [[] for _ in range(n+1)]
for i in range(n):
    if par[i] == -1: rt=i; continue
    chd[par[i]].append(i)
vs[int(input())] = 1
cnt = 0
dfs(rt)
print(cnt)