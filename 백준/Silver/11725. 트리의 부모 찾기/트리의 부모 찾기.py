from collections import deque

n = int(input())
tr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tr[a].append(b); tr[b].append(a)
pr = [0]*(n+1)
vs = [0]*(n+1)
q = deque([1])
vs[1] = 1
while q:
    x = q.popleft()
    for i in tr[x]:
        if not vs[i]: vs[i] = 1; pr[i] = x; q.append(i)
for i in range(2, n+1): print(pr[i])