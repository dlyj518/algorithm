import sys
input = sys.stdin.readline

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
rst = 0

def dfs(y, x, n):
    global rst
    rst = max(rst, n)
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < r and 0 <= nx < c and vs[mp[ny][nx]] == 0:
            vs[mp[ny][nx]] = 1
            dfs(ny, nx, n+1)
            vs[mp[ny][nx]] = 0

r, c = map(int, input().split())
mp = [list(map(lambda x: ord(x)-65, input().strip())) for _ in range(r)]
vs = [0]*26
vs[mp[0][0]] = 1
dfs(0, 0, 1)
print(rst)