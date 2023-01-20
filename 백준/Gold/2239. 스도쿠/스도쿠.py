def chk(i):
    if i == len(zr): return 1
    y, x = zr[i][0], zr[i][1]
    z = (y // 3) * 3 + x // 3
    for k in range(1, 10):
        if rw[y][k] and cl[x][k] and ss[z][k]:
            rw[y][k] = 0; cl[x][k] = 0; ss[z][k] = 0
            mp[y][x] = k
            if chk(i + 1): return 1
            rw[y][k] = 1; cl[x][k] = 1; ss[z][k] = 1
            mp[y][x] = 0
    return 0

mp = [list(map(int, input())) for _ in range(9)]
rw = [[1] * 10 for _ in range(9)]
cl = [[1] * 10 for _ in range(9)]
ss = [[1] * 10 for _ in range(9)]
zr = []
for i in range(9):
    for j in range(9):
        x = mp[i][j]
        if x:
            rw[i][x] = 0
            cl[j][x] = 0
            ss[(i // 3) * 3 + j // 3][x] = 0
        else: zr.append((i, j))
chk(0)
for i in range(9): print(*mp[i], sep='')