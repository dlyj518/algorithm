from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
rd = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, p = map(int,input().split())
    rd[s].append((e, p))
s, e = map(int,input().split())
cs = [1e9]*(n+1)
cs[s] = 0
q = [(0, s)]
while q:
    c, v = heappop(q)
    if c > cs[v]: continue
    for l, d in rd[v]:
        if cs[l] > c + d: cs[l] = c + d; heappush(q, (c + d, l))
print(cs[e])