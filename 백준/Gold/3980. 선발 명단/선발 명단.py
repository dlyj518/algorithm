def dfs(i, x):
    global mx
    if i == 11: mx = max(mx, x)
    for j in range(11):
        if vs[j] and mt[i][j]: vs[j] = 0; dfs(i + 1, x + mt[i][j]); vs[j] = 1

for _ in range(int(input())):
    mt = [list(map(int, input().split())) for _ in range(11)]
    vs, mx = [1] * 11, 0
    dfs(0, 0)
    print(mx)