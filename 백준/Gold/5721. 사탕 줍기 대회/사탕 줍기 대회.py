import sys
input = sys.stdin.readline
while 1:
    n, m = map(int, input().split())
    if n == m == 0: break
    dpi = [[0]*2 for _ in range(n)]
    for i in range(n):
        dpj = [[0]*2 for _ in range(m)]
        mp = list(map(int, input().split()))
        dpj[0][1] = mp[0]
        for j in range(1, m):
            dpj[j][0] = max(dpj[j-1])
            dpj[j][1] = dpj[j-1][0] + mp[j]
        if not i: dpi[i][1] = max(dpj[-1])
        else:
            dpi[i][0] = max(dpi[i-1])
            dpi[i][1] = dpi[i-1][0] + max(dpj[-1])
    print(max(dpi[-1]))