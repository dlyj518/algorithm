from collections import deque

dy,dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(y,x):
    q = deque([(y,x)])
    mp[y][x] = 2
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and mp[ny][nx] == 1:
                q.append((ny, nx))
                cnt += 1
                mp[ny][nx] = cnt
    return cnt

n = int(input())
mp = [list(map(int, input())) for _ in range(n)]
rst = []
for i in range(n):
    for j in range(n):
        if mp[i][j] == 1: rst.append(bfs(i,j))
rst.sort()
print(len(rst))
print(*rst, sep='\n')