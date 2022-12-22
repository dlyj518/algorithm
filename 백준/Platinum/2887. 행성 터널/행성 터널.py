import sys
input = sys.stdin.readline

def fnd(x):
    if pr[x] != x: return fnd(pr[x])
    return x

n = int(input())
pt = []
rd = []
pr = list(range(n+1))
for i in range(n): pt.append([i] + list(map(int, input().split())))
for i in range(1, 4):
    pt = sorted(pt, key=lambda x: x[i])
    for j in range(n-1):
        rd.append((abs(pt[j+1][i] - pt[j][i]), pt[j+1][0], pt[j][0]))
rd.sort()
rst = 0
for c, a, b in rd:
    a, b = map(fnd, (a, b))
    if a != b:
        if a < b: pr[b] = a
        else: pr[a] = b
        rst += c
print(rst)