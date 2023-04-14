def fl(y, x):
    global ch
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < n and 0 <= nx < n: ch[ny][nx] += 1

n = int(input())
mp = [''] * n
mp[0] = input()
ch = [[0] * n for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
print(mp[0])
for y in range(1, n):
    for x in range(n):
        if mp[y - 1][x] == '#': fl(y - 1, x)
    for x in range(n):
        mp[y] += '#' if ch[y - 1][x] % 2 else '.'
    print(mp[y])