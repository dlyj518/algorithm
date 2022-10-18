def dfs(i, c, l):
    global rst
    l = l[:]
    if c == m: rst.append(l); return
    for j in range(i, n+1): dfs(j, c+1, l+[j])

n, m = map(int, input().split())
rst = []
dfs(1, 0, [])
for i in rst: print(*i)