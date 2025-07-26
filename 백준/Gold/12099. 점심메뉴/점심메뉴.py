import sys
input = sys.stdin.readline

n, q = map(int, input().split())
mn = []
for _ in range(n):
    a, b  = map(int, input().split())
    mn.append([a, b])

mn.sort()

for _ in range(q):
    u, v, x, y  = map(int, input().split())
    s, e = 0, n - 1
    while s <= e:
        m = (s + e) // 2
        if mn[m][0] < u: s = m + 1
        else: e = m - 1
    l = s
    
    s, e = 0, n - 1
    while s <= e:
        m = (s + e) // 2
        if mn[m][0] <= v: s = m + 1
        else: e = m - 1
    r = e

    c = 0
    for i in range(l, r + 1):
        if x <= mn[i][1] <= y: c += 1
    
    print(c)