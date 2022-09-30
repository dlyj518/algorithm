import sys
input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(y, x, s, c=1):
    global mx, mxp
    if c == 4: mx = max(mx, s); return
    if s + mxp*(4-c) < mx: return
    vs[y][x] = 1
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0 <= ny < n and 0 <= nx < m and not vs[ny][nx]: dfs(ny, nx, s+mp[ny][nx], c+1)
    vs[y][x] = 0

def tsp(y, x):
    global mx
    for i in range(4):
        s = mp[y][x]
        for j in range(4):
            if i != j:
                ny, nx = y+dy[j], x+dx[j]
                if not(0 <= ny < n) or not(0 <= nx < m): break
                s += mp[ny][nx]
        else: mx = max(mx, s)


n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
vs = [[0]*m for _ in range(n)]
mx = 0
mxp = max(sum(mp,[]))
for i in range(n):
    for j in range(m):
        dfs(i, j, mp[i][j])
        tsp(i, j)
print(mx)