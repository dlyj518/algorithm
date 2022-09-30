import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    rst, vs = 0, [0]*(n+1)
    vs[x] = 1
    while q:
        y = q.popleft()
        for i in nd[y]:
            if not vs[i]: rst+= 1; vs[i] = 1; q.append(i)
    return rst

n, m = map(int, input().split())
nd = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    nd[b].append(a)
rst, ps, mx = set(), set(), 0
for i in range(1, n+1):
    if i in ps: continue
    x = bfs(i)
    if x > mx: mx = x; rst.clear(); rst.add(i)
    if x == mx: rst.add(i)
print(*rst)