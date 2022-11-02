from collections import deque

n,k = map(int,input().split())
q = deque([n])
vs = [0]*100001
rst = 0
lmt = 1e6
while q:
    x = q.popleft()
    if vs[x] > lmt: continue
    if x == k: rst += 1; lmt = vs[k]
    for i in [x - 1, x + 1, x * 2]:
        if 0 > i or i > 100000 : continue
        if vs[i] == 0 or vs[i] >= vs[x] + 1 :
            vs[i] = vs[x]+1
            q.append(i)
print(vs[k], rst)