from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])
rst = -1
while q:
    x, c = q.popleft()
    if x == b: rst = c; break
    if x > b: continue
    q.append((x*2, c+1))
    q.append((x*10+1, c+1))
print(rst)