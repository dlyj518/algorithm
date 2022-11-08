from collections import deque
from itertools import combinations
from copy import deepcopy

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = []
q = []
r = []
rst = 0
mp = [list(map(int, input().split())) for _ in range(n)]
c = sum(mp, []).count(0)
for i in range(n):
    for j in range(m):
        if mp[i][j] == 2: q.append((i, j, c-3))
        if mp[i][j] == 0: r.append((i, j))
for (y1, x1), (y2, x2), (y3, x3) in combinations(r, 3):
    np = deepcopy(mp)
    np[y1][x1] = np[y2][x2] = np[y3][x3] = 1
    qq = deque(q[:])
    while qq:
        y, x, c = qq.popleft()
        if c <= rst: continue
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and not np[ny][nx]:
                np[ny][nx] = 2
                qq.append((ny, nx, c-1))
    cc = sum(np, []).count(0)
    rst = max(rst, cc)
print(rst)