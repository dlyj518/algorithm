v, e = map(int, input().split())
dr = [[1e8]*v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    dr[a-1][b-1] = c
for k in range(v):
    for i in range(v):
        for j in range(v): dr[i][j] = min(dr[i][j], dr[i][k] + dr[k][j])
x = min([dr[i][i] for i in range(v)])
print(x) if x < 1e8 else print(-1)