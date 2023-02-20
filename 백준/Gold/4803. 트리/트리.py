import sys
input = sys.stdin.readline

def dfs(p, x):
    vs[x] = 0
    for i in pr[x]:
        if i == p: continue
        if not vs[i]: return 0
        if not dfs(x, i): return 0
    return 1

t = 0
while 1:
    t += 1
    n, m = map(int, input().split())
    if n == m == 0: break
    pr = [[] for _ in range(n + 1)]
    vs = [1] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        pr[a].append(b); pr[b].append(a)
    c = 0
    for i in range(1, n + 1):
        if vs[i] and dfs(0, i): c += 1
    if c == 0: print(f'Case {t}: No trees.')
    elif c == 1: print(f'Case {t}: There is one tree.')
    else: print(f'Case {t}: A forest of {c} trees.')