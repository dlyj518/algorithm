import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
from pprint import pprint
import heapq

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]

n = int(input())
mp = []
fs = [0]*7
sl, exp = 2, 0
for i in range(n):
    mp.append(list(map(int,input().split())))
    for j in range(n):
        if mp[i][j] == 9: sk = deque([(i, j, 0)])
        elif mp[i][j] != 0: fs[mp[i][j]] += 1
while 1:
    if sum(fs[:sl]) == 0: break
    vs = [[0] * n for _ in range(n)]
    vs[sk[0][0]][sk[0][1]] = 1
    mp[sk[0][0]][sk[0][1]] = 0
    tmp = []
    st = -1
    while sk:
        y, x, c = sk.popleft()
        if c == st: break
        if 0 < mp[y][x] < sl:
            st = c + 1
            tmp.append((y, x, c))
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and not vs[ny][nx] and mp[ny][nx] <= sl:
                vs[ny][nx] = 1; sk.append((ny, nx, c+1))
    tmp.sort(key = lambda x: (x[0], x[1]))
    y, x, c = tmp[0]
    fs[mp[y][x]] -= 1
    exp += 1
    mp[y][x] = 9
    sk = deque([(y, x, c)])
    if exp == sl: sl += 1; exp = 0
print(sk[0][2])