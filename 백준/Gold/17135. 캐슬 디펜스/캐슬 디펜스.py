from collections import deque
from copy import deepcopy

dy, dx = [0, -1, 0], [-1, 0, 1]

def atck(x):
    q = deque([(nn-1, x, 1)])
    while q:
        y, x, c = q.popleft()
        if mp[y][x] == 1: st.add((y, x)); return
        if c == d: continue
        for dd in range(3):
            ny, nx = y+dy[dd], x+dx[dd]
            if 0 <= ny < n and 0 <= nx < m: q.append((ny, nx, c+1))

n, m, d = map(int, input().split())
mpo = [list(map(int, input().split())) for _ in range(n)]
s = sum(mpo,[]).count(1)
rst, mx = 0, 0
for a in range(n):
    if mpo[a].count(1) != 0: c = n-a; break

for i in range(m-2):
    for j in range(i+1, m-1):
        for k in range(i+2, m):
            ls = [i, j, k]
            mp = deepcopy(mpo)
            nn, rst, ss = n, 0, s
            for l in range(c):
                st = set()
                for ll in ls:
                    if ss != 0: atck(ll)
                for y, x in st:
                    mp[y][x] = 0; ss -= 1; rst += 1
                mp = mp[:nn-1]
                nn -= 1
            if mx < rst: mx = rst
print(mx)