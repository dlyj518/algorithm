import sys
input = sys.stdin.readline

n, a, l = map(int, input().split())
dp = [[-1] * (l + 1) for _ in range(n + 1)]
dp[0][l] = a
xy = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    x, y = xy[i]
    for j in range(1, l + 1):
        if dp[i][j] == -1: continue
        if y >= 0 and j > y and dp[i + 1][j - y] < dp[i][j]:
            dp[i + 1][j - y] = dp[i][j]
        if x >= 0:
            mx = dp[i][j] - x
            if y < 0 and mx < 0: mx = 0
            if dp[i + 1][j] < mx:
                dp[i + 1][j] = mx
rst = []
for ll in range(1, l + 1):
    if dp[n][ll] != -1:
        print('YES')
        aa = dp[n][ll]
        for i in range(n, 0, -1):
            x, y = xy[i - 1]
            if x == -1: rst.append('L'); ll += y
            elif y == -1: rst.append('A'); aa += x
            elif ll + y <= l and dp[i - 1][ll + y] == aa: rst.append('L'); ll += y
            else: rst.append('A'); aa += x
        print(''.join(rst[::-1])); break
else: print('NO')