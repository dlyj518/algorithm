from collections import deque

dy, dx, d = [-1, 0, 1, 0], [0, 1, 0, -1], 1
n = int(input())
k = int(input())
mp = [[1] * n for _ in range(n)]
mp[0][0] = 0
ap, cm = [], deque([])
sn = deque([(0, 0)])
for _ in range(k):
    y, x = map(int, input().split())
    mp[y - 1][x - 1] = 9
l = int(input())
for _ in range(l): cm.append(input().split())
t, q, y, x = 0, 1, 0, 0
z, c = cm.popleft()
z = int(z)
while q:
    t += 1
    y += dy[d]; x += dx[d]
    if 0 <= y < n and 0 <= x < n:
        sn.append((y, x))
        if mp[y][x]:
            if mp[y][x] != 9:
                a, b = sn.popleft()
                mp[a][b] = 1
            mp[y][x] = 0
        else: q = 0; break
    else: break
    if t == z:
        d += 1 if c == 'D' else - 1
        d %= 4
        if cm:
            z, c = cm.popleft()
            z = int(z)
print(t)