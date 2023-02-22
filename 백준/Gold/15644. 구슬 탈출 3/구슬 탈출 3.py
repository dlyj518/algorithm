from collections import deque
dy, dx, dr = [-1, 1, 0, 0], [0, 0, -1, 1], ['U', 'D', 'L', 'R']
def run(y, x, d):
    c = 0
    while 1:
        y += dy[d]; x += dx[d]
        if mp[y][x] == 'O': c = -1; break
        if mp[y][x] == '#': y -= dy[d]; x -= dx[d]; break
        c += 1
    return y, x, c

n, m = map(int, input().split())
mp = []
for i in range(n):
    mp.append(list(input()))
    for j in range(m):
        if mp[i][j] == 'R': ry, rx = i, j
        if mp[i][j] == 'B': by, bx = i, j
        if mp[i][j] == 'O': ot = (i, j)
q = deque([[ry, rx, by, bx, -1, 0, []]])

rst = 0
while q:
    ry, rx, by, bx, dd, cc, ll = q.popleft()
    l = ll[:]
    if cc > 9: continue
    for d in range(4):
        if dd == d: continue
        if dd == (d // 2 + 1) * 2 - d % 2 - 1: continue
        nry, nrx, rc = run(ry, rx, d)
        nby, nbx, bc = run(by, bx, d)
        if bc < 0: continue
        if rc < 0: rst = cc+1; break
        if nry == nby and nrx == nbx:
            if rc > bc: nry -= dy[d]; nrx -= dx[d]
            else: nby -= dy[d]; nbx -= dx[d]
        q.append([nry, nrx, nby, nbx, d, cc+1, l + [dr[d]]])
    if rst: break
if rst: print(rst); print(''.join(l) + dr[d])
else: print(-1)