dy, dx = [.5, -.5, 0, 0], [0, 0, -.5, .5]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    mp = []
    for i in range(n):
        x, y, d, k = map(int, input().split())
        mp.append([y, x, d, k])
    rst = 0
    while len(mp) >= 2:
        for i in range(len(mp)):
            mp[i][0], mp[i][1] = mp[i][0]+dy[mp[i][2]], mp[i][1]+dx[mp[i][2]]
        lc = {}
        for a in mp:
            if lc.get((a[0], a[1]),0) == 0: lc[(a[0], a[1])] = [a]
            else: lc[(a[0], a[1])].append(a)
        mp = []
        for dc in lc:
            if len(lc[dc]) > 1:
                for dd in lc[dc]: rst += dd[3]
            else:
                if -1000 <= lc[dc][0][0] <= 1000 and -1000 <= lc[dc][0][1] <= 1000:  mp.append(lc[dc][0])
    print(f'#{tc} {rst}')