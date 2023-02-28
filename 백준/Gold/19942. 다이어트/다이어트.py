def dfs(i, p, f, s, v, c, ls):
    global mn, l
    if c > mn: return
    if m[0] <= p and m[1] <= f and m[2] <= s and m[3] <= v and mn > c: l = ls ; mn = c; return
    if i == n: return
    dfs(i + 1, p + fd[i][0], f + fd[i][1], s + fd[i][2], v + fd[i][3], c + fd[i][4], ls + [i + 1])
    dfs(i + 1, p, f, s, v, c, ls)

n = int(input())
m = list(map(int, input().split()))
fd = []
for _ in range(n): fd.append(list(map(int, input().split())))
mn, l = 1e9, []
dfs(0, 0, 0, 0, 0, 0, [])
if mn == 1e9: print(-1)
else:
    print(mn)
    for i in l: print(i, end = ' ')