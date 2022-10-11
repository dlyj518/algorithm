from itertools import permutations
from copy import deepcopy

def spin(r, c, s):
    for i in range(1, s+1):
        tmp = mm[r-i][c+i]
        mm[r-i][c-i+1 : c+i+1] = mm[r-i][c-i : c+i]
        for j in range(r-i, r+i): mm[j][c-i] = mm[j+1][c-i]
        mm[r+i][c-i : c+i] = mm[r+i][c-i+1 : c+i+1]
        for j in range(r+i, r-i+1, -1): mm[j][c+i] = mm[j-1][c+i]
        mm[r-i+1][c+i] = tmp

n, m, d = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
sp = []
rst = 100*m
for _ in range(d): sp.append(list(map(int, input().split())))
for ls in permutations(sp, d):
    mm = deepcopy(mp)
    mn = 100*m
    for r, c, s in ls: spin(r-1, c-1, s)
    for i in range(n): mn = min(mn, sum(mm[i]))
    rst = min(rst, mn)
print(rst)