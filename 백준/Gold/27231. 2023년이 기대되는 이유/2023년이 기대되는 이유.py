def dfs(i, x, s):
    if i == l - 1: rt.add(s + x); return
    dfs(i + 1, n[i + 1], s + x)
    dfs(i + 1, 10 * x + n[i + 1], s)

t = int(input())
for _ in range(t):
    n = list(map(int, input()))
    if sum(n) == 1 or max(n) == 1: print('Hello, BOJ 2023!'); continue
    l = len(n)
    if l == 1: print(1); continue
    rt = set()
    dfs(0, n[0], 0)
    rs = 1; m = 2
    while 1:
        lf = sum(map(lambda x: x ** m, n))
        if lf > max(rt): break
        if lf in rt: rs += 1
        m += 1; bf = lf
    print(rs)