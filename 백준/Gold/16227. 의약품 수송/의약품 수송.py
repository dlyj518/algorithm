from heapq import heappush, heappop

n, k = map(int, input().split())
rd = [[] for _ in range(n + 2)]
vs = [[1e9] * 101 for _ in range(n + 2)]
for _ in range(k):
    u, v, t = map(int, input().split())
    if t <= 100: rd[u].append([v, t]); rd[v].append([u, t])
q = [(0, 0, 0)]
while q:
    c, d, i = heappop(q)
    if vs[i][d] < 1e9: continue
    vs[i][d] = c
    for j, y in rd[i]:
        if d + y > 100: dd = y; t = c + y + 5
        else: dd = d + y; t = c + y
        if vs[j][dd] > 1e5: heappush(q, (t, dd, j))
print(min(vs[n + 1]))