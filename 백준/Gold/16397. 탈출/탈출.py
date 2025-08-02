from collections import deque
import math

n, t, g = map(int, input().split())
vs = list([0] * 100000)
q = deque([[n, 0]])
while q:
    i, s = q.popleft()
    if vs[i]: continue
    else: vs[i] = 1
    if i == g: print(s); break
    if s == t: continue
    if i < 99999 and not vs[i + 1]: q.append([i + 1, s + 1])
    if i: 
        i2 = i * 2 - 10 ** int(math.log10(i * 2))
        if i * 2 <= 99999 and not vs[i2]: q.append([i2, s + 1])
else: print('ANG')