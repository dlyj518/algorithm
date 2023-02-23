dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
n, m, x, y, k = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
cm = list(map(lambda x: x - 1, map(int, input().split())))
dc = [0] * 6
sp = [[0, 4, 2, 5, 3, 1], [0, 5, 2, 4, 1, 3], [1, 2, 3, 0, 4, 5], [3, 0, 1, 2, 4, 5]]
for d in cm:
    nx, ny = x + dx[d], y + dy[d]
    if not(0 <= nx < n and 0 <= ny < m): continue
    dc = [dc[sp[d][i]] for i in range(6)]
    if mp[nx][ny]: dc[3] = mp[nx][ny]; mp[nx][ny] = 0
    else: mp[nx][ny] = dc[3]
    print(dc[1])
    x, y = nx, ny