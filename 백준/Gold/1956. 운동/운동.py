from heapq import *
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
dp = [[1e8]*(v+1) for _ in range(v+1)]
rd = {i: [] for i in range(v+1)}
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    dp[a][b] = c
    rd[a].append((c, b))
    heappush(q, (c, a, b))
while q:
    c, a, b = heappop(q)
    if a == b: print(c); break
    if c > dp[a-1][b]: continue
    for k, r in rd[b]:
        if c + k < dp[a][r]:
            dp[a][r] = c + k; heappush(q, (c+k, a, r))
else: print(-1)