import heapq
n = int(input())
q = []
t = 0
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(q, (-p, d))
    t = max(t, d)
r = [0]*(t+1)
while q:
    p, d = heapq.heappop(q)
    while d > 0:
        if not r[d]: r[d] = -p; break
        d -= 1
print(sum(r))