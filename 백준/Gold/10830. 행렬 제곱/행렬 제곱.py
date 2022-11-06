def pd(x, y):
    r = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): r[i][j] += x[i][k] * y[k][j]
            r[i][j] %= 1000
    return r
def sq(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n): a[i][j] %= 1000
        return a
    h = sq(a, b//2)
    if b % 2: return pd(pd(h, h), a)
    return pd(h, h)

n, b = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]
s = sq(a, b)
for x in sq(a, b): print(*x)