from heapq import *

n = int(input())
t = [[] for i in range(10001)]
for i in range(n):
    p, d = map(int, input().split())
    t[d].append(p)
q = []
rst = 0
for i in range(10000, 0, -1):
    for x in t[i]: heappush(q, -x)
    if q: rst += -heappop(q)
print(rst)