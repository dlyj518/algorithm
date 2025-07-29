n, k = map(int, input().split())
ans = set()

def dfs(x, ls):
    if x == n: ans.add(ls); return
    if x < n: dfs(x + 1, ls + (1,))
    if x + 1 < n: dfs(x + 2, ls + (2,))
    if x + 2 < n: dfs(x + 3, ls + (3,))

dfs(0, ())
if len(ans) < k: print(-1)
else:
    ans = sorted(list(ans))
    print(*ans[k - 1], sep='+')