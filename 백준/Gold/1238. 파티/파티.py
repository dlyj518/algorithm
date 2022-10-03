import heapq

n, m, x = map(int, input().split())
tr = [[] for _ in range(n+1)]
vs = [-1]*(n+1)
for _ in range(m):
    s, e, w = map(int, input().split())
    tr[s].append([e,w])
rst = [0]*(n+1)
for i in range(1, n + 1):
    # 목표지점 > 목표지점은 할 필요 없음
    if i == x: continue
    ds = [1e7] * (n + 1)
    q = []
    heapq.heappush(q, [0, i])
    while q:
        w, s = heapq.heappop(q)
        # 도착지점 이미 왔으면 break
        if s == x: break
        for e, ew in tr[s]:
            if ds[e] > w + ew:
                ds[e] = w + ew
                heapq.heappush(q, [ds[e], e])
    rst[i] += ds[x]
# 목표지점 > 지역 경로
ds = [1e7] * (n + 1)
q = []
heapq.heappush(q, [0, x])
while q:
    w, s = heapq.heappop(q)
    for e, ew in tr[s]:
        if ds[e] > w + ew:
            ds[e] = w + ew
            heapq.heappush(q, [ds[e], e])
for i in range(1, n + 1): rst[i] += ds[i]
print(max(rst))