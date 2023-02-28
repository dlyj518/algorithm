def chk(i, j, k, l, c):
    s = 0
    for y in range(i, j):
        for x in range(k, l):
            if mp[y][x] == '.': s += 1
    return 0 if s == c else 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    mp = [list(input()) for _ in range(n)]
    nx, ny = m, n; xx = xy = 0
    for i in range(n):
        for j in range(m):
            if mp[i][j] == '#':
                nx = min(nx, j); xx = max(xx, j); ny = min(ny, i); xy = max(xy, i)
    if xy - ny != xx - nx: print(0); continue
    x, c = xy - ny, 0
    for i in range(ny, xy + 1):
        for j in range(nx, xx + 1):
            if mp[i][j] == '.': c += 1
    for i in range(1, x + 1):
        if i ** 2 == c: y = i; break
    else: print(0); continue
    p1 = chk(ny, ny + y, nx, nx + y, c)
    p2 = chk(ny, ny + y, xx - y + 1, xx + 1, c)
    p3 = chk(xy - y + 1, xy + 1, nx, nx + y, c)
    p4 = chk(xy - y + 1, xy + 1, xx - y + 1, xx + 1, c)
    if not p1 * p2 * p3 * p4: print(1)
    else: print(0)