import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
rd = [[] for _ in range(v+1)]
vs = [0]+[1e8]*v
vs[s] = 0
for _ in range(e):
    x, y, z = map(int, input().split())
    rd[x].append([y, z])
q = [(0, s)]
while q:
    (c, a) = heapq.heappop(q)
    for b, d in rd[a]:
        if vs[b] > c+d:
            vs[b] = c+d
            heapq.heappush(q, (c+d, b))
for i in vs[1:]:
    if i != 1e8: print(i)
    else: print('INF')