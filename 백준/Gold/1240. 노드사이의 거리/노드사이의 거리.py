def dfs(s, e, n=0):
    rst = 0
    if s == e: return n
    vs[s] = 1
    x = bool(eg[s])
    if eg[s]:
        for i in range(len(eg[s])):
            if not vs[eg[s][i]]: rst = max(rst,dfs(eg[s][i], e, n + lg[s][i]))
    return rst

n, m = map(int, input().split())
eg = [[] for _ in range(n+1)]
lg = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, l = map(int, input().split())
    eg[a].append(b); lg[a].append(l)
    eg[b].append(a); lg[b].append(l)
for i in range(m):
    vs = [0] * (n + 1)
    s, e = map(int, input().split())
    print(dfs(s, e))