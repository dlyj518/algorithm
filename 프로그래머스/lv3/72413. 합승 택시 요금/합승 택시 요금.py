import heapq

def daij(s, n, tr):
    q = []
    ds = [1e9]*(n+1)
    ds[s] = 0
    heapq.heappush(q, [s, 0])
    while q:
        x, c = heapq.heappop(q)
        for y, d in tr[x].items():
            if ds[y] > c+d: ds[y] = c+d; heapq.heappush(q, [y, c+d])
    return ds

def solution(n, s, a, b, fares):
    tr = {i:{} for i in range(n+1)}
    for x, y, z in fares:
        tr[x][y] = z; tr[y][x] = z
    answer = 1e9
    ds = daij(s, n, tr)
    for k in range(1, n+1):
        dk = daij(k, n, tr)
        answer = min(answer, ds[k]+dk[a]+dk[b])
    return answer