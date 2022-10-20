n, d, k, c = map(int, input().split())
cb = []
for _ in range(n): cb.append(int(input()))
i = 0
dk = min(d, k)
rst = 0
while i < n:
    mn, mx = min(n, i+k), max(n, i+k) % n
    ls = set(cb[i : mn] + cb[:mx])
    if c not in ls: ls.add(c)
    rst = max(rst, len(ls))
    i += 1
print(rst)