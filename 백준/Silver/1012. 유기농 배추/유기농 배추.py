import sys
sys.setrecursionlimit(10000) 

drx = [-1, 1, 0, 0]
dry = [0, 0, -1, 1]

def dfs(x,y):
    for i in range(4):
        nx = x + drx[i]
        ny = y + dry[i]
        if 0<=nx<m and 0<=ny<n:
            if mp[ny][nx] == 1:
                mp[ny][nx] = -1
                dfs(nx,ny)


t = int(input())
for tc in range(t):
    m,n,k = map(int,input().split())
    mp = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x,y = map(int,input().split())
        mp[y][x] = 1
    for i in range(m):
        for j in range(n):
            if mp[j][i] > 0:
                dfs(i,j)
                cnt += 1
    print(cnt)