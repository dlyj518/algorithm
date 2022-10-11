from itertools import combinations
from collections import deque

def bfs(lst):
    global chk
    vs = [0]*(n+1)
    q = deque([lst[0]])
    vs[lst[0]] = 1
    cnt, rt = 1, 0
    while q:
        x = q.popleft()
        rt += pp[x]
        for z in tr[x]:
            if z in lst and not vs[z]: vs[z]=1; cnt += 1; q.append(z)
    if cnt == len(lst): return rt
    return 0

n = int(input())
pp = [0]+list(map(int, input().split()))
tr = [[] for _ in range(n+1)]
ll = set(range(1, n+1))
sp = sum(pp)
rst, chk = sp, 0
for i in range(n):
    m, *l = map(int, input().split())
    tr[i+1] = l
for a in range(1, n//2+1):
    for ls in combinations(ll, a):
        dl = tuple(ll - set(ls))
        x, y = bfs(ls), bfs(dl)
        if x != 0 and y != 0 : chk = 1; rst = min(rst, abs(x-y))
rst = -1 if chk == 0 else rst
print(rst)