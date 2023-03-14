import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
q = []
for _ in range(n):
    i, s, e = map(int, input().split())
    heappush(q, (s, e))
r = []
rs = 0
while q:
    s, e = heappop(q)
    while r:
        if r[0] > s: break
        heappop(r)
    heappush(r, e)
    rs = max(rs, len(r))
print(rs)