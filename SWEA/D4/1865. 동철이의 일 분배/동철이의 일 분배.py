def prob(x, p = 100):
    global rst
    if p * mxp[x] <= rst: return
    if x == n: rst = p
    for i in range(n):
        if vs[i] == 0:
            vs[i] = 1; prob(x+1, p * mp[x][i] / 100)
            vs[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    mxp = [max(mp[i])/100 for i in range(n)][::-1]
    for i in range(1,n):
        mxp[i] *= mxp[i-1]
    mxp = mxp[::-1]
    mxp.append(1)
    vs, rst = [0]*n, 0
    prob(0)
    print(f'#{tc} {rst:.6f}')