def fs(x):
    if x == pr[x]: return x
    return fs(pr[x])

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(m)]
    pr = list(range(n + 1))
    for s, e in ls:
        pr[fs(e)] = fs(s)
    rst = len(set([fs(i) for i in range(n + 1)])) - 1
    print(f'#{tc} {rst}')