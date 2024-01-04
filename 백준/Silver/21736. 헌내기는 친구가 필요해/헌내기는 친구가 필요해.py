from collections import deque

n, m = map(int, input().split())
mp = []
vs = [[1] * m for _ in range(n)]
for i in range(n):
    mp.append(list(input()))
    for j in range(m):
        if mp[i][j] == 'I': (w, z) = (i, j)
vs[w][z] = 0
r = 0

q = deque()
q.append((w, z))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
while q:
    a, b = q.popleft()
    for i in range(4):
        y, x = a + dy[i], b + dx[i]
        if 0 <= y < n and 0 <= x < m and vs[y][x] and mp[y][x] != 'X':
            if mp[y][x] == 'P': r += 1
            vs[y][x] = 0; q.append((y, x))
print(r) if r else print('TT')