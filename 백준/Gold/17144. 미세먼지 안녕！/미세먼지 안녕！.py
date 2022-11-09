import sys
input = sys.stdin.readline
from copy import deepcopy

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
r, c, t = map(int, input().split())
mp = []
ac = []
for i in range(r):
    mp.append(list(map(int, input().split())))
    for j in range(c):
        if mp[i][j] == -1: ac.append((i,j))
for tt in range(t):
    np = [[0] * c for _ in range(r)]
    for a, b in ac: np[a][b] = -1
    for y in range(r):
        for x in range(c):
            if mp[y][x] > 0:
                a = mp[y][x]
                np[y][x] += a
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < r and 0 <= nx < c and mp[ny][nx] >= 0:
                        np[ny][nx] += a//5
                        np[y][x] -= a//5
    y, x = ac[0]
    if y > 0:
        yy, xx = y, x
        y -= 1
        for d in range(4):
            while 1:
                ny, nx = y + dy[d], x + dx[d]
                if ny < 0 or ny > yy or nx < 0 or nx >= c: break
                if np[ny][nx] == -1: np[y][x] = 0; break
                np[y][x] = np[ny][nx]
                y, x = ny, nx
    y, x = ac[1]
    if y < r-1:
        yy, xx = y, x
        y += 1
        for d in range(4):
            while 1:
                ny, nx = y + dy[(2-d)%4], x + dx[(2-d)%4]
                if ny < yy or ny >= r or nx < 0 or nx >= c: break
                if np[ny][nx] == -1: np[y][x] = 0; break
                np[y][x] = np[ny][nx]
                y, x = ny, nx
    mp = deepcopy(np)
print(sum(sum(mp, []))+2)