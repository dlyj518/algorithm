from collections import deque

n, k = map(int, input().split())
q = deque([n])
vs = [-1]*100001
pr = [-1]*100001
vs[n] = 0
while q:
    x = q.popleft()
    if x == k: break
    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i <= 100000 and vs[i] == -1:
            vs[i] = vs[x] + 1
            pr[i] = x
            q.append(i)
rst = [k]
while 1:
    if pr[x] == -1: break
    rst.append(pr[x])
    x = pr[x]
print(vs[k])
print(*rst[::-1])