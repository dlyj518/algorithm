import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[-1] * 51 for _ in range(51)]
dp[0][0] = 0
for _ in range(m):
    r, b, d = map(int, input().split())
    for i in range(50, r - 1, -1):
        for j in range(50, b - 1, -1):
            if dp[i - r][j - b] == -1: continue
            dp[i][j] = max(dp[i][j], dp[i - r][j - b] + d)
ls = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    ls.append((max(dp[x][y], 0), i))
for a in sorted(ls):
    print(f'{a[1]} {a[0]}')