from copy import deepcopy

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def mv1(mp, vs, y, x, d):
    nm = mp[y][x]
    mp[y][x] = 0
    while 1:
        y += dy[d]; x += dx[d]
        if (0 <= y < n) and (0 <= x < n):
            if mp[y][x] == 0: continue
            if mp[y][x] == nm and vs[y][x]: mp[y][x] = nm*2; vs[y][x] = 0; break
        y -= dy[d]; x -= dx[d]; mp[y][x] = nm
        break

def mv(mp, d, m, c=0):
    global mx
    if mx < m: mx = m
    if mx >= m**(6-c): return
    mp = deepcopy(mp)
    vs = [[1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if d == 0: mv1(mp, vs, j, i, d)
            if d == 1: mv1(mp, vs, n-1-j, i, d)
            if d == 2: mv1(mp, vs, i, j, d)
            if d == 3: mv1(mp, vs, i, n-1-j, d)
    m = max(sum(mp, []))
    for dd in range(4): mv(mp, dd, m, c+1)


n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]
mx = max(sum(mp, []))
for i in range(4): mv(mp, i, mx)
print(mx)