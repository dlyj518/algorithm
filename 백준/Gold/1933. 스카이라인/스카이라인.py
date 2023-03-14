from heapq import heappush, heappop
n = int(input())
ar, hh, ed = [], [], []
for i in range(n):
    l, h, r = map(int, input().split())
    ar.append((l, 0, i))
    ar.append((r, 1, i))
    hh.append(h); ed.append(r)
ar.sort(key = lambda x: (x[0], x[1], -hh[x[2]]))
nh = 0
rs, q = [], []
ch = set()
for i in range(len(ar)):
    p, d, h = ar[i]
    if not d:
        if nh < hh[h]: nh = hh[h]; rs.append((p, nh))
        heappush(q, (-hh[h], ed[h]))
    else:
        ch.add(p)
        while q:
            if q[0][1] not in ch: break
            heappop(q)
        if not q:
            if nh: nh = 0; rs.append((p, nh))
        else:
            if -q[0][0] != nh:
                nh = -q[0][0]; rs.append((p, nh))
for r in rs: print(r[0], r[1], end=' ')