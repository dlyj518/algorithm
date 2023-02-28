import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())
rd = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, l, k = map(int, input().split())
    rd[a].append((b, l * 2520, k))
    rd[b].append((a, l * 2520, k))
q = [(0, 1, 1)]
vs = [[1e14] * 11 for _ in range(n + 1)]
vs[1][1] = 0
while q:
    t, x, s = heappop(q)
    if vs[x][s] < t: continue
    for y, l, k in rd[x]:
        for i in range(-1, 2):
            ss = s + i
            if not 1 <= ss <= k: continue
            nt = t + l // ss
            if vs[y][ss] > nt:
                vs[y][ss] = nt
                heappush(q, (nt, y, ss))
r = min(vs[n])
print(r // 2520, end = '')
print((f'{round((r % 2520) / 2520, 9):.9f}')[1:])