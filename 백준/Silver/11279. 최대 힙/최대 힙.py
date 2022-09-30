import sys
input = sys.stdin.readline
import heapq

n = int(input())
hp = []
for _ in range(n):
    x = int(input())
    if x != 0: heapq.heappush(hp, -x); continue
    if len(hp)>0: print(-heapq.heappop(hp))
    else: print(0)