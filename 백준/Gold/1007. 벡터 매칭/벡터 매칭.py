from itertools import combinations as comb

for _ in range(int(input())):
    n = int(input())
    vx, vy = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        vx.append(x); vy.append(y)
    rst = 300000
    cb = list(comb(range(n), n // 2))
    for t in cb[:len(cb) // 2]:
        sx = sy = 0
        for i in t: sx += vx[i]; sy += vy[i]
        sx = sx * 2 - sum(vx); sy = sy * 2 - sum(vy)
        vt = (sx ** 2 + sy ** 2) ** .5
        rst = min(rst, vt)
    print(rst)