def chk(i, j):
    if mp[i][j] == 'C': return 1
    return 0

di = (-1, 0, 1)
n, m = map(int, input().split())
mp = []
for i in range(n):
    ls = list(input())
    if 'R' in ls: y, x = i, ls.index('R')
    mp.append(ls)
dp = [[0]*m for _ in range(n)]
vs = [[0]*m for _ in range(n)]
vs[y][x] = 1
rst = -1
for j in range(x+1, m):
    for i in range(n):
        if mp[i][j] == '#': continue
        mx = -1
        for d in range(3):
            ii = i + di[d]
            if 0 <= ii < n and vs[ii][j-1]:
                mx = max(mx, dp[ii][j-1])
                vs[i][j] = 1
        if vs[i][j]: dp[i][j] = mx + chk(i, j)
        if mp[i][j] == 'O': rst = max(rst, mx)
print(rst)