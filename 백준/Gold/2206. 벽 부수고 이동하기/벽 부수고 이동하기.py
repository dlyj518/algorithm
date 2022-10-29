from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = [list(input()) for _ in range(n)]
vs = [[[0,0] for _ in range(m)] for _ in range(n)]
vs[0][0][1] = 1
q = deque([(0,0,1)])
rst = -1
while q:
    y, x, t = q.popleft()
    if (y, x) == (n-1, m-1): rst = vs[y][x][t]; break
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if not(0 <= ny < n) or not(0 <= nx < m): continue
        if mp[ny][nx] == '1' and t == 1:
            vs[ny][nx][0] = vs[y][x][1] + 1
            q.append((ny, nx, 0))
        elif mp[ny][nx] == '0' and vs[ny][nx][t] == 0:
            vs[ny][nx][t] = vs[y][x][t] + 1
            q.append((ny, nx, t))
print(rst)