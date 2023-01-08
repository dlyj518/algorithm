from collections import defaultdict as dt, deque
import sys
input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    r, c = h + 2, w + 2
    mp = [['.'] * c]
    dr = dt(list)
    for i in range(1, h +1):
        mp.append(list('.' + input() + '.'))
        for j in range(1, w + 1):
            if 'A' <= mp[i][j] <= 'Z': dr[mp[i][j]].append((i, j))
    mp.append(['.'] * c)
    ky = list(input())
    if ky != ['0']:
        for k in ky:
            for i, j in dr[k.upper()]: mp[i][j] = '.'
    vs = [[1] * c for _ in range(r)]
    q = deque([(0, 0)])
    rs = 0
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < r and 0 <= nx < c and vs[ny][nx]:
                if mp[ny][nx] == '*': continue
                vs[ny][nx] = 0
                if 'A' <= mp[ny][nx] <= 'Z': continue
                if mp[ny][nx] == '$': rs += 1
                elif 'a' <= mp[ny][nx] <= 'z':
                    for i, j in dr[mp[ny][nx].upper()]:
                        mp[i][j] = '.'
                        if not vs[i][j]: q.append((i, j))
                q.append((ny, nx))
    print(rs)