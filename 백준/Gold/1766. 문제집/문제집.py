from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pr = [[] for _ in range(n+1)]
ch = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    pr[a].append(b); ch[b] += 1
q = []
rst = []
for i in range(1, n+1):
    if not ch[i]: q.append(i)
while q:
    x = heappop(q)
    rst.append(x)
    for y in pr[x]:
        ch[y] -= 1
        if not ch[y]: heappush(q, y)
print(*rst)