import heapq

t = int(input())
for tc in range(1, t+1):
    n, m, x = map(int, input().split())
    wd = [[] for _ in range(n+1)]
    for _ in range(m):
        xx, y, c = map(int, input().split())
        wd[xx].append([y, c])
    rst = [0]*(n+1)
    for i in range(1, n+1):
        if i == x: continue
        ds = [1e7]*(n+1)
        q = []
        heapq.heappush(q, [0, i])
        while q:
            w, s = heapq.heappop(q)
            if s == x: break
            for e, ew in wd[s]:
                if ds[e] > w + ew:
                    ds[e] = w + ew
                    heapq.heappush(q, [ds[e], e])
        rst[i] += ds[x]
    ds = [1e7] * (n + 1)
    q = []
    heapq.heappush(q, [0, x])
    while q:
        w, s = heapq.heappop(q)
        for e, ew in wd[s]:
            if ds[e] > w + ew:
                ds[e] = w + ew
                heapq.heappush(q, [ds[e], e])
    for i in range(1, n+1): rst[i] += ds[i]
    print(f'#{tc} {max(rst)}')