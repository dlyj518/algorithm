from collections import deque
import sys
input = sys.stdin.readline

def spin(a, n):
    if not a: return mp
    t = [[0]*n for _ in range(n)]
    for y in range(0, n, a):
        for x in range(0, n, a):
            for i in range(a):
                for j in range(a):
                    t[y+i][x+j] = mp[y+a-1-j][x+i]
    return t

def chk():
    global dr
    vs = [[1]*n for _ in range(n)]
    mx = 0
    for y in range(n):
        for x in range(n):
            if mp[y][x] and vs[y][x]:
                vs[y][x] = 0
                c, q = 1, deque([(y, x)])
                while q:
                    y, x = q.popleft()
                    for d in dr:
                        ny, nx = y + d[0], x + d[1]
                        if 0 <= ny < n and 0 <= nx < n and mp[ny][nx] and vs[ny][nx]:
                            vs[ny][nx] = 0; c += 1; q.append((ny, nx))
                mx = max(mx, c)
    return mx

dr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
n, q = map(int, input().split())
n = 2**n
mp = [list(map(int, input().split())) for _ in range(n)]
m = list(map(int, input().split()))
for l in m:
    k = 2**l
    mp = spin(k, n)
    cnt = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            for d in dr:
                ny, nx = y + d[0], x + d[1]
                if 0 <= ny < n and 0 <= nx < n and mp[ny][nx]: cnt[y][x] += 1
    for y in range(n):
        for x in range(n):
            if mp[y][x] and cnt[y][x] < 3: mp[y][x] -= 1
print(sum(sum(mp, [])))
print(chk())