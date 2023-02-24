n, m = map(int, input().split())
y, x, d = map(int, input().split())
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
mp = [list(map(int, input().split())) for _ in range(n)]
r = 0
while 1:
    if not mp[y][x]: r += 1; mp[y][x] = -1
    c = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not mp[ny][nx]: c += 1
    if not c:
        nd = (d + 2) % 4
        if mp[y + dy[nd]][x + dx[nd]] == 1: break
        y += dy[nd]; x += dx[nd]
    else:
        d = (d - 1) % 4
        if not mp[y + dy[d]][x + dx[d]]: y += dy[d]; x += dx[d]
print(r)