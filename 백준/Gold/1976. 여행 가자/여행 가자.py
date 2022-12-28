def fnd(x):
    if x == pr[x]: return x
    pr[x] = fnd(pr[x])
    return pr[x]

def uni(x, y):
    x, y = fnd(x), fnd(y)
    if x < y: pr[y] = x
    else: pr[x] = y

n, m = int(input()), int(input())
pr = list(range(n))
for i in range(n):
    rt = list(map(int, input().split()))
    for j in range(i+1, n):
        if rt[j]: uni(i, j)
pl = list(map(int, input().split()))
for i in range(n): pr[i] = fnd(pr[i])
pr = [0] + pr
bg = pr[pl[0]]
for p in pl:
    if pr[p] != bg: print('NO'); break
else: print('YES')