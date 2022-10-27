from collections import deque
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
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
rl, bl = [(ry, rx)], [(by, bx)]
q = deque([[ry, rx, by, bx, rl, bl, -1, 0]])

rst = 0
while q:
    ry, rx, by, bx, rl, bl, dd, cc = q.popleft()
    if cc > 9: continue
    for d in range(4):
        if dd == d: continue
        if dd == (d//2+1)*2-d%2-1: continue
        nrl = rl[:]; nbl = bl[:]
        nry, nrx, rc = run(ry, rx, d)
        nby, nbx, bc = run(by, bx, d)
        if bc < 0: continue
        if rc < 0: rst = cc+1; break
        if nry == nby and nrx == nbx:
            if rc > bc: nry -= dy[d]; nrx -= dx[d]
            else: nby -= dy[d]; nbx -= dx[d]
        nrl.append((nry, nrx)); nbl.append((nby, nbx))
        q.append([nry, nrx, nby, nbx, nrl, nbl, d, cc+1])
    if rst: break
if rst: print(rst)
else: print(-1)
