import sys
input = sys.stdin.readline
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(i, j):
    rs = [[-1] * (ww) for _ in range(hh)]
    rs[i][j] = 0
    q = deque([(i, j)])
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < hh and 0 <= nx < ww and mp[ny][nx] != '*' and rs[ny][nx] == -1:
                if mp[ny][nx] == '.' or mp[ny][nx] == '$':
                    rs[ny][nx] = rs[y][x]
                    q.appendleft((ny, nx))
                if mp[ny][nx] == '#':
                    rs[ny][nx] = rs[y][x] + 1
                    q.append((ny, nx))
    return rs

for _ in range(int(input())):
    h, w = map(int,input().split())
    hh, ww = h + 2, w + 2
    mp = [list('.' * (w + 2))]
    for i in range(h):
        mp.append(list('.' + input().strip() + '.'))
    mp.append(list('.' * (ww)))
    l = []
    for i in range(hh):
        for j in range(ww):
            if mp[i][j] == '$':
                l.append((i,j))
    a = bfs(l[0][0], l[0][1])
    b = bfs(l[1][0], l[1][1])
    c = bfs(0, 0)
    ans = sys.maxsize
    for i in range(hh):
        for j in range(ww):
            if a[i][j] != -1 and b[i][j] != -1 and c[i][j] != -1:
                res = a[i][j] + b[i][j] + c[i][j]
                if mp[i][j] == '*': continue
                if mp[i][j] == '#': res -= 2
                ans = min(ans, res)
    print(ans)