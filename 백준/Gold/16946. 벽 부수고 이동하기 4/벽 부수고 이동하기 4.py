def bfs(y, x, c):
    q = [(y, x)]
    vs[y][x] = 1
    for i, j in q:
        for d in range(4):
            ni, nj = i + dy[d], j + dx[d]
            if 0 <= ni < n and 0 <= nj < m and not mp[ni][nj] and not vs[ni][nj]: vs[ni][nj] = 1; q.append((ni, nj))
    s = len(q)
    for i, j in q: vs[i][j] = c
    dt.append(s)


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = [list(map(int, list(input()))) for _ in range(n)]
rs = [[0] * m for _ in range(n)]
vs = [[0] * m for _ in range(n)]
dt = [0, 0]
c = 2
for i in range(n):
    for j in range(m):
        if mp[i][j] == 1:
            s = set()
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < n and 0 <= nx < m and mp[ny][nx] != 1:
                    if not vs[ny][nx]: bfs(ny, nx, c); c += 1
                    s.add(vs[ny][nx])
            for x in s: rs[i][j] += dt[x]
            rs[i][j] = (rs[i][j] + 1) % 10

for i in range(n):
    for j in range(m): print(rs[i][j], end = '')
    print()