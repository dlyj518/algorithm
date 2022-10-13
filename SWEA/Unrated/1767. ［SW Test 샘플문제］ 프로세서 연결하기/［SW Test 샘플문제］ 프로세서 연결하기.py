dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def sign(x):
    if x<0: return -1
    else: return 1

def rb(ls):
    for a in ls:
        y,x = a
        mp[y][x] = 0


def root(i, c, mn):
    global rst
    if c > rst[0]: rst[0] = c; rst[1] = mn
    elif c == rst[0]: rst[1] = min(rst[1], mn)
    if i >= len(cr): return
    y, x = cr[i]
    for d in range(4):
        cnt = 0
        ls = []
        ny, nx = y + dy[d], x + dx[d]
        while 0 <= ny < n and 0 <= nx < n:
            if mp[ny][nx] != 0: rb(ls); break
            mp[ny][nx] = -1
            ls.append([ny,nx])
            ny += dy[d]; nx += dx[d]
            cnt += 1
        else:
            root(i+1, c+1, mn + cnt)
            rb(ls)
    root(i+1, c, mn)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    cr = []
    rst = [0, 144]
    for i in range(1, n-1):
        for j in range(1, n-1):
            if mp[i][j] == 1: cr.append([i, j])
    root(0, 0, 0)
    print(f'#{tc} {rst[1]}')