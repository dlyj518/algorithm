dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    mp = [[0]*n for _ in range(n)]
    md = n//2
    mp[md-1][md-1] = mp[md][md] = 2
    mp[md-1][md] = mp[md][md-1] = 1
    for _ in range(m):
        x, y, bw = map(int, input().split())
        x -= 1; y -= 1
        mp[y][x] = bw
        ls = []
        for i in range(8):
            ny, nx = y, x
            while True:
                ny += dy[i]
                nx += dx[i]
                if not(0 <= ny < n) or not(0 <= nx < n) : ls = []; break
                if mp[ny][nx] == 0: ls = []; break
                if mp[ny][nx] == bw: break
                else: ls.append([ny, nx])
            for yy, xx in ls: mp[yy][xx] = bw
    bl = sum(mp, []).count(1)
    wh = sum(mp, []).count(2)
    print(f'#{tc} {bl} {wh}')