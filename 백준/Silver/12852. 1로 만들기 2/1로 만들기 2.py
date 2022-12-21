from collections import deque

n = int(input())
vs = [0]*1000001
vs[n] = [n]
q = deque([n])
while q:
    x = q.popleft()
    if x == 1: break
    if not x % 3 and not vs[x // 3]: vs[x // 3] = vs[x] + [x // 3]; q.append(x // 3)
    if not x % 2 and not vs[x // 2]: vs[x // 2] = vs[x] + [x // 2]; q.append(x // 2)
    if not vs[x - 1]: vs[x - 1] = vs[x] + [x - 1]; q.append(x - 1)
print(len(vs[1]) - 1)
print(*vs[1])