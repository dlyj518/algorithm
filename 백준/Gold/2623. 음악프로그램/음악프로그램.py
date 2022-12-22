n, m = map(int, input().split())
pr = [set() for _ in range(n+1)]
for _ in range(m):
    a, *b = map(int, input().split())
    for i in range(a-1):
        pr[b[i+1]].add(b[i])
rst = []
q = []
while 1:
    for i in range(1, n+1):
        if not pr[i]: q.append(i)
    if len(q) == 0: break
    while q:
        x = q.pop()
        rst.append(x)
        for i in range(1, n+1):
            if x in pr[i]: pr[i].remove(x)
        pr[x] = [-1]
if len(rst) == n: print(*rst, sep='\n')
else: print(0)