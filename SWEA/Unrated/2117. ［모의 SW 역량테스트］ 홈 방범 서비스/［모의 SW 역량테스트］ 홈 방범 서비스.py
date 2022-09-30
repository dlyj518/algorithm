from collections import deque

dy, dx = [-1, 1, 0 ,0], [0, 0, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    rst = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, n+2):
                q.append([i, j, 1])
                h = mp[i][j]
                vs = [[0] * n for _ in range(n)]
                vs[i][j] = 1
                while q:
                    [y, x, c] = q.popleft()
                    if c == k: continue
                    for d in range(4):
                        ny, nx = y+dy[d], x+dx[d]
                        if 0<=ny<n and 0<=nx<n and not vs[ny][nx]:
                            h += mp[ny][nx]
                            vs[ny][nx] = 1
                            q.append([ny, nx, c+1])
                if h * m - k*k - (k-1)**2 >= 0: rst = max(rst, h)
    print(f'#{tc} {rst}')