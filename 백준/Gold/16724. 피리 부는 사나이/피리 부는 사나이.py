import sys
sys.setrecursionlimit(10**6)

def fds(i, j, l):
    global rs
    if vs[i][j]: return
    vs[i][j] = 1
    i += dr[mp[i][j]][0]; j += dr[mp[i][j]][1]
    if vs[i][j]:
        if (i, j) in l: rs += 1
    else: l.append((i, j)); fds(i, j, l)

dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
n, m = map(int, input().split())
mp = [list(input()) for _ in range(n)]
vs = [[0]*m for _ in range(n)]
rs = 0
for i in range(n):
    for j in range(m): fds(i, j, [(i, j)])
print(rs)