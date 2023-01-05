def bus(ls):
    rst = 0; t = 0
    for l, m in ls:
        while 1:
            if not t: rst += l * 2
            if k >= m + t: t += m; break
            m += t - k; t = 0
    return rst

n, k, s = map(int, input().split())
rp = {}; rm = {}
for _ in range(n):
    i, j = map(int, input().split())
    if i > s: rp[i - s] = j
    else: rm[s - i] = j
rp = sorted(rp.items(), reverse=True)
rm = sorted(rm.items(), reverse=True)
print(bus(rm) + bus(rp))