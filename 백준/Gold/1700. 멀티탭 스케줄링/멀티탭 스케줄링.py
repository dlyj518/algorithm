n, k = map(int, input().split())
dt = {i:[] for i in range(1, k + 1)}
ls = list(map(int, input().split()))
for i in range(n, k): dt[ls[i]].append(i)
for i in range(1, k + 1): dt[i].append(k+1)
mt = []
rst = 0
for i in range(k):
    if ls[i] in mt: continue
    if len(mt) < n: mt.append(ls[i]); continue
    mn = mi = 0
    for j in range(n):
        k = 0
        while 1:
            d = dt[mt[j]][k]
            if d <= i: k += 1; continue
            if mn < d: mn = d; mi = j
            break
    rst += 1
    mt[mi] = ls[i]
print(rst)