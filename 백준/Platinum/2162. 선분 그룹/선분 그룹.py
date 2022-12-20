def ccw(a, b, c): return (b[0] - a[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - a[1])
def pdcw(a, b, c, d): return ccw(a, b, c) * ccw(a, b, d)
def crch(a, b):
    if pdcw(a[0], a[1], b[0], b[1]) <= 0 and pdcw(b[0], b[1], a[0], a[1]) <= 0:
        if not pdcw(a[0], a[1], b[0], b[1]) and not pdcw(b[0], b[1], a[0], a[1]):
            if max(a[0][0], a[1][0]) >= min(b[0][0], b[1][0]) and max(b[0][0], b[1][0]) >= min(a[0][0], a[1][0]) and \
                    max(a[0][1], a[1][1]) >= min(b[0][1], b[1][1]) and max(b[0][1], b[1][1]) >= min(a[0][1], a[1][1]):
                return 1
        else: return 1
    return 0
def f_pr(x):
    if pr[x] != x: return f_pr(pr[x])
    return x

def mg(a, b):
    a = f_pr(a); b = f_pr(b)
    if a < b: pr[b] = a
    else: pr[a] = b

pt = []
n = int(input())
pr = list(range(n))
for _ in range(n):
    p = list(map(int, input().split()))
    pt += [[p[:2], p[2:]]]
for i in range(1, n):
    p = pt[i]; lg = set()
    for j in range(i):
        if pr[i] == pr[j]: continue
        q = pt[j]
        if crch(p, q): mg(j, i)
for i in range(n): pr[i] = f_pr(i)
dt = {}
for a in pr:
    if dt.get(a, 0): dt[a] += 1
    else: dt[a] = 1
print(len(dt))
print(max(dt.values()))