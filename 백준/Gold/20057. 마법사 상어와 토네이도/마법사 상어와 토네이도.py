n = int(input())
dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
mp = [list(map(int, input().split())) for _ in range(n)]
lf = [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1),
      (2, 0, 2), (1, -1, 10), (1, 0, 7), (1, 1, 1), (0, -2, 5)]
rt = [(y, -x, p) for y, x, p in lf]
up = [(x, y, p) for y, x, p in lf]
dn = [(-x, y, p) for y, x, p in lf]
dr = {0: lf, 1: dn, 2: rt, 3: up}

d, c, r, m = 0, 0, 0, 1
y = x = n//2
rst = 0
while 1:
    y += dy[d]; x += dx[d]
    if not 0 <= y < n or not 0 <= x < n: break
    s = mp[y][x]; mp[y][x] = 0
    ns = s
    for yy, xx, p in dr[d]:
        if 0 <= y+yy < n and 0 <= x+xx < n:
            mp[y+yy][x+xx] += s * p // 100
        else: rst += s * p // 100
        ns -= s * p // 100
    if 0 <= y+dy[d] < n and 0 <= x+dx[d] < n:
        mp[y+dy[d]][x+dx[d]] += ns
    else: rst += ns
    c += 1
    if c == m: r += 1; d = (d + 1) % 4; c = 0
    if r > 1: r = 0; m += 1
print(rst)