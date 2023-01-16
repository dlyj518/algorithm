from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
vs = [[1] * m for _ in range(n)]
rs = 0
for i in range(n):
    for j in range(m):
        if not mp[i][j] and vs[i][j]:
            vs[i][j] = 0
            q = deque([(i, j)])
            rs += 1
            while q:
                y, x = q.pop()
                for d in range(4):
                    ny, nx = (y + dy[d]) % n, (x + dx[d]) % m
                    if not mp[ny][nx] and vs[ny][nx]: vs[ny][nx] = 0; q.append((ny, nx))
print(rs)