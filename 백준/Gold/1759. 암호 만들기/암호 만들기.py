def dfs(y, i, j, k):
    if i + j == n and i and j > 1: print(y); return
    if k == m: return
    if x[k] in ['a', 'e', 'i', 'o', 'u']: dfs(y + x[k], i + 1, j, k + 1)
    else: dfs(y + x[k], i, j + 1, k + 1)
    dfs(y, i, j, k + 1)

n, m = map(int, input().split())
x = sorted(list(input().split()))
dfs('', 0, 0, 0)