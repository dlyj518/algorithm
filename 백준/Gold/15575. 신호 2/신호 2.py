def ds(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

n = int(input())
xx = {}
for _ in range(n):
    x, y = map(int, input().split())
    if xx.get(x, 0):
        if xx[x][0] > y: xx[x][0] = y
        if xx[x][1] < y: xx[x][1] = y
    else: xx[x] = [y, y]
dp = [[0] * 2 for _ in range(len(xx))]
it = sorted(list(xx.items()), key=lambda x: x[0])
for i in range(1, len(xx)):
    w, z = it[i - 1]
    x, y = it[i]
    for j in range(2):
        dp[i][j] = max(dp[i - 1][0] + ds(w, z[0], x, y[j]), dp[i - 1][1] + ds(w, z[1], x, y[j]))
print(max(dp[-1]))