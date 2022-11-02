from collections import deque

n = int(input())
tm = [0]
pr = [[] for _ in range(n+1)]
rst = [0]*(n+1)
for i in range(1, n+1):
    l = list(map(int, input().split()))
    tm.append(l[0])
    for j in range(1, len(l)-1):
        pr[i].append(l[j])
q = deque([])
while 1:
    for i in range(1, n+1):
        if not pr[i]: q.append(i)
    if len(q) == 0: break
    while q:
        x = q.pop()
        rst[x] += tm[x]
        for i in range(1, n+1):
            if x in pr[i]: pr[i].remove(x); rst[i] = max(rst[i], rst[x])
        pr[x] = [-1]
print(*rst[1:])