from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = []
q = deque([])
for i in range(n):
    mp.append(list(input()))
    for j in range(m):
        if mp[i][j] == 'J': jj = (i, j, 0, 1);
        if mp[i][j] == 'F': q.append((i, j, 1, 1))
q.append(jj)
vs = [[1]*m for _ in range(n)]
rst = 'IMPOSSIBLE'
while q:
    y, x, t, c = q.popleft()
    if not t and (y in [0, n-1] or x in [0,m-1]): rst = c; break
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if not(0 <= ny < n) or not(0 <= nx < m): continue
        if mp[ny][nx] == '.' and t: mp[ny][nx] = 'F'; q.append((ny, nx, t, c+1))
        if mp[ny][nx] == '.' and not t and vs[ny][nx]: vs[ny][nx] = 0; q.append((ny, nx, t, c+1))
print(rst)