import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
rd =[sorted(list(map(int,input().split()))) for _ in range(n)]
l = int(input())
rd.sort(key=lambda x:x[1])
h, rs = [], 0
for r in rd:
    if r[1] - r[0] > l: continue
    if not h: heappush(h, r); continue
    while h[0][0] < r[1] - l:
        heappop(h)
        if not h: break
    heappush(h, r)
    rs = max(rs, len(h))
print(rs)