n, m = map(int, input().split())
mp = [list(input().strip()) for _ in range(n)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0

for u in range(26):
    if u == 12: continue
    a = chr(65 + u)
    for v in range(26):
        if v == 14 or u == v: continue
        b = chr(65 + v)
        c = 0
        for y in range(n):
            for x in range(m):
                if mp[y][x] == a:
                    for i in range(8):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        nny = ny + dy[i]
                        nnx = nx + dx[i]
                        if 0 <= ny < n and 0 <= nx < m and mp[ny][nx] == b and 0 <= nny < n and 0 <= nnx < m and mp[nny][nnx] == b: c += 1
        ans = max(ans, c)
print(ans)