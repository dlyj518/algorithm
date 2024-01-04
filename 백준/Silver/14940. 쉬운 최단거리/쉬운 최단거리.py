from collections import deque

n, m = map(int, input().split())
mp = []
rs = [[-1] * m for _ in range(n)]
for i in range(n):
    mp.append(list(map(int, input().split())))
    for j in range(m):
        if mp[i][j] == 2: (w, z) = (i, j)
        if not mp[i][j]: rs[i][j] = 0
rs[w][z] = 0

q = deque()
q.append((w, z))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
while q:
    a, b = q.popleft()
    for i in range(4):
        y, x = a + dy[i], b + dx[i]
        if 0 <= y < n and 0 <= x < m and rs[y][x] < 0:
            rs[y][x] = rs[a][b] + 1; q.append((y, x))
for i in range(n): print(*rs[i])