import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jew = []
for _ in range(n): heapq.heappush(jew, list(map(int, input().split())))
bag = []
for _ in range(k): bag.append(int(input()))
bag.sort()
rst = 0
tmp = []
for b in bag:
    while jew and b >= jew[0][0]: heapq.heappush(tmp, -heapq.heappop(jew)[1])
    if tmp: rst -= heapq.heappop(tmp)
    elif not jew: break
print(rst)