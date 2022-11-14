n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
rd = [[9999]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    rd[a][b] = l
    rd[b][a] = l
for i in range(n+1): rd[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if rd[i][j] > rd[i][k] + rd[k][j]: rd[i][j] = rd[i][k] + rd[k][j]
rst = 0
for i in range(1, n+1):
    s = 0
    for j in range(1, n+1):
        if rd[i][j] <= m: s += t[j]
    rst = max(rst, s)
print(rst)