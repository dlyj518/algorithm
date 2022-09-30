from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
mp = [list(input()) for _ in range(n)]
vs = [[0]*n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if vs[i][j] == 0:
            q = deque([(i, j, mp[i][j])])
            vs[i][j] = 2 if mp[i][j] == 'B' else 1
            cnt1 += 1
            while q:
                y, x, c = q.popleft()
                for a in range(4):
                    ny, nx = y+dy[a], x+dx[a]
                    if 0 <= ny < n and 0 <= nx < n and vs[ny][nx] == 0 and mp[ny][nx] == c:
                        q.append((ny, nx, mp[ny][nx]))
                        vs[ny][nx] = 2 if mp[ny][nx] == 'B' else 1
cnt2 = 0
for i in range(n):
    for j in range(n):
        if vs[i][j] != 0:
            q = deque([(i, j, vs[i][j])])
            cnt2 += 1
            while q:
                y, x, c = q.popleft()
                for a in range(4):
                    ny, nx = y+dy[a], x+dx[a]
                    if 0 <= ny < n and 0 <= nx < n and vs[ny][nx] == c:
                        q.append((ny, nx, vs[ny][nx]))
                        vs[ny][nx] = 0
print(f'{cnt1} {cnt2}')