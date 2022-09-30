from copy import deepcopy

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
cc = [[], [[0], [1], [2], [3]], [[0,1], [2,3]], [[0,3], [1,3], [1,2], [0,2]], [[1,2,3], [0,1,2], [0,2,3], [0,1,3]], [[0,1,2,3]]]

def wtch(arr, ls, y, x):
    for i in ls:
        ny, nx = y, x
        while 1:
            ny += dy[i]; nx += dx[i]
            if not(0 <= ny < n) or not(0 <= nx < m): break
            if arr[ny][nx] == 6: break
            if arr[ny][nx] == 0: arr[ny][nx] = 7

def dfs(arr, c=0):
    global mn
    if c == len(ct): mn = min(mn, sum(arr, []).count(0)); return
    tmp = deepcopy(arr)
    y, x, cn = ct[c]
    for i in cc[cn]:
        wtch(tmp, i, y, x)
        dfs(tmp, c+1)
        tmp = deepcopy(arr)

n, m = map(int, input().split())
ct, mp = [], []
for i in range(n):
    mp.append(list(map(int, input().split())))
    for j in range(m):
        if mp[i][j] not in [0,6] : ct.append([i, j, mp[i][j]])
mn = m*n
dfs(mp)
print(mn)