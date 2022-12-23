n = int(input())
pt = [list(map(int, input().split())) for _ in range(n)]
pt += [pt[0]]
rst = 0
for i in range(n): rst += pt[i][0] * pt[i+1][1] - pt[i][1] * pt[i+1][0]
print(round(abs(rst) / 2, 2))