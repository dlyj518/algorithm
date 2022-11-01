import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ds = [[1e9] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if ds[a-1][b-1] > c: ds[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: ds[i][i] = 0
            if ds[i][j] > ds[i][k] + ds[k][j]: ds[i][j] = ds[i][k] + ds[k][j]
for i in range(n):
    for j in range(n):
        if ds[i][j] == 1e9: print(0, end=' ')
        else: print(ds[i][j], end=' ')
    print()