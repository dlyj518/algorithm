from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = []
cz, rst = 0, 0
for i in range(n):
    mp.append(list(map(int, input().split())))
    for j in range(m):
        if mp[i][j]: cz += 1
while cz:
    rst += 1
    vs = [[1]*m for _ in range(n)]
    vs[0][0] = 0
    mt = set()
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < n and 0 <= nx < m and mp[ny][nx] >= 0 and vs[ny][nx]:
                if mp[ny][nx]:
                    vs[ny][nx] += 1
                    if vs[ny][nx] > 2: mt.add((ny, nx))
                else:
                    vs[ny][nx] = 0
                    q.append((ny, nx))
    for y, x in mt: mp[y][x] = 0; cz -= 1
print(rst)