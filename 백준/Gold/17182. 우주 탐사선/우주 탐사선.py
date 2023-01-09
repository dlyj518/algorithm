def dfs(x, c, r):
    global rst
    if c == n:
        if rst > r: rst = r
        return
    if r > rst: return
    for i in range(n):
        if vs[i]:
            vs[i] = 0
            dfs(i, c + 1, r + mp[x][i])
            vs[i] = 1

n, k = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
for l in range(n):
    for i in range(n):
        for j in range(n):
            if mp[i][j] > mp[i][l] + mp[l][j]: mp[i][j] = mp[i][l] + mp[l][j]
vs = [1] * n
vs[k] = 0
rst = 1e9
dfs(k, 1, 0)
print(rst)