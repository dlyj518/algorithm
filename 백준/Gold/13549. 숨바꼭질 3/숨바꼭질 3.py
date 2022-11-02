from collections import deque

n,k = map(int,input().split())
q = deque([n])
vs = [-1]*100001
vs[n] = 0
while q:
    x = q.popleft()
    if x == k: print(vs[k]); break
    if 0 <= x*2 <= 100000 and vs[x*2] == -1:
        vs[x*2] = vs[x]
        q.appendleft(x*2)
    for i in [x - 1, x + 1]:
        if 0 > i or i > 100000 : continue
        if vs[i] == -1:
            vs[i] = vs[x]+1
            q.append(i)