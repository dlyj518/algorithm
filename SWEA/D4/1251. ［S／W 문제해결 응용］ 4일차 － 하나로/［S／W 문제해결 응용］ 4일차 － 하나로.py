def dist(a, b):
    return (xx[a]-xx[b])**2 + (yy[a]-yy[b])**2
def fs(x):
    if x == pr[x]: return x
    return fs(pr[x])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    xx = list(map(int, input().split()))
    yy = list(map(int, input().split()))
    gp = []
    e = float(input())
    for i in range(n-1):
        for j in range(i+1, n):
            gp.append([i, j, dist(i,j)])
    gp.sort(key=lambda x:x[2])
    pr = list(range(n+1))
    rst = 0
    for u, v, w in gp:
        if fs(u) != fs(v):
            rst += w
            pr[fs(v)] = fs(u)
    print(f'#{tc} {rst*e:.0f}')