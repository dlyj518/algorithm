from itertools import combinations as cb

def fnd(x):
    if x == pr[x]: return x
    return fnd(pr[x])
def dst(i, j):
    d = ((pt[i][0] - pt[j][0])**2 + (pt[i][1] - pt[j][1])**2)**.5
    rd.append((d, i, j))

n = int(input())
pr = list(range(n))
pt = [list(map(float, input().split())) for _ in range(n)]
rd = []
for i, j in list(cb(range(n), 2)): dst(i, j)
rd.sort()
rs = 0
for d, i, j in rd:
    i, j = fnd(i), fnd(j)
    if i == j: continue
    rs += d
    if i < j: pr[j] = i
    else: pr[i] = j
print(rs)