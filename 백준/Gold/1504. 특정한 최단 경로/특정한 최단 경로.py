import heapq
import sys
input = sys.stdin.readline

def dai(s):
    q = []
    ds = [1e8]*(n+1)
    ds[s] = 0
    heapq.heappush(q, [s, 0])
    while q:
        x, d = heapq.heappop(q)
        for a, dd in tr[x].items():
            if ds[a] > d+dd: ds[a] = d+dd; heapq.heappush(q, [a, d+dd])
    return ds

n, e = map(int, input().split())
tr = {i:{} for i in range(n+1)}
for _ in range(e):
    a, b, c = map(int, input().split())
    tr[a][b] = c
    tr[b][a] = c
x, y = map(int, input().split())
ds = dai(1)
dx = dai(x)
dy = dai(y)
rst = min(ds[x]+dx[y]+dy[n], ds[y]+dy[x]+dx[n])
rst = -1 if rst >= 1e8 else rst
print(rst)