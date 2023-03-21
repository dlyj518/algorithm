from collections import deque

n, m, k = map(int, input().split())
mp = [list(input()) for _ in range(n)]
vs = [[1e7] * m for _ in range(n)]
y1, x1, y2, x2 = map(int, input().split())
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([(y1 - 1, x1 - 1)])
vs[y1 - 1][x1 - 1] = 0
c = 1
while q:
    y, x = q.popleft()
    for d in range(4):
        for i in range(1, k + 1):
            ny, nx = y + dy[d] * i, x + dx[d] * i
            if 0 <= ny < n and 0 <= nx < m and  mp[ny][nx] == '.' and vs[ny][nx] > vs[y][x]:
                if vs[ny][nx] == 1e7:
                    vs[ny][nx] = vs[y][x] + 1; q.append((ny, nx))
            else: break
print(-1 if vs[y2 - 1][x2 - 1] == 1e7 else vs[y2 - 1][x2 - 1])