import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

n, l, r = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
lc = [[0] * n for _ in range(n)]
c, rst = 0, -1
while c != n**2:
    c, dc = 0, {}
    vs = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not vs[i][j]:
                c += 1; vs[i][j] = c
                dc[c] = [[i, j, mp[i][j]]]
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()
                    for d in range(4):
                        ny, nx = y+dy[d], x+dx[d]
                        if 0 <= ny < n and 0 <= nx < n and not vs[ny][nx] and not lc[ny][nx] and l <= abs(mp[ny][nx] - mp[y][x]) <= r:
                            vs[ny][nx] = c; lc[ny][nx] = 1; q.append([ny, nx])
                            dc[c].append([ny, nx, mp[ny][nx]])
    for d in dc:
        if len(dc[d]) > 1:
            lc = [[0] * n for _ in range(n)]
            mix = sum([dc[d][i][2] for i in range(len(dc[d]))]) // len(dc[d])
            for i in range(len(dc[d])):
                mp[dc[d][i][0]][dc[d][i][1]] = mix
    rst += 1
print(rst)