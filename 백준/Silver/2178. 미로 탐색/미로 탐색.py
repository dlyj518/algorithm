from collections import deque

dy,dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n,m = map(int,input().split())
mp = [list(map(int, input())) for _ in range(n)]
q = deque([(0, 0)])
mp[0][0] = 2
while q:
    y,x = q.popleft()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<m and mp[ny][nx] == 1:
            q.append((ny,nx))
            mp[ny][nx] = mp[y][x]+1
print(mp[n-1][m-1]-1)