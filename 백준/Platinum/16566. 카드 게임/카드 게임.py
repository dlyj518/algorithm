def fnd(x):
    if x == pr[x]: return x
    pr[x] = fnd(pr[x])
    return pr[x]

def uni(a, b):
    if b > n: b = 1
    a = fnd(a); b = fnd(b)
    pr[a] = b

def bin(x):
    s, e = 0, m - 1
    while s <= e:
        md = (s + e) // 2
        if ls[md] <= x: s = md + 1
        else: e = md - 1
    return s

n, m, k = map(int, input().split())
pr = list(range(m + 1))
ls = list(map(int, input().split()))
rc = list(map(int, input().split()))
ls.sort()

for c in rc:
    i = bin(c)
    ci = fnd(i)
    print(ls[ci])
    uni(ci, ci + 1)