from itertools import combinations as cb

n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
rst = 0
for a, b, c in cb(range(m), 3):
    sm = 0
    for i in range(n):
        sm += max(ls[i][a], ls[i][b], ls[i][c])
    if rst < sm: rst = sm
print(rst)