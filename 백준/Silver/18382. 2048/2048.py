dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def mv1(mp, vs, y, x, d):
    global rst
    nm = mp[y][x]
    mp[y][x] = 0
    while 1:
        y += dy[d]; x += dx[d]
        if (0 <= y < 4) and (0 <= x < 4):
            if mp[y][x] == 0: continue
            if mp[y][x] == nm and vs[y][x]: mp[y][x] = nm*2; vs[y][x] = 0; rst += nm*2; break
        y -= dy[d]; x -= dx[d]; mp[y][x] = nm
        break

def mv(mp, d):
    vs = [[1]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if d == 0: mv1(mp, vs, j, i, d)
            if d == 1: mv1(mp, vs, 3-j, i, d)
            if d == 2: mv1(mp, vs, i, j, d)
            if d == 3: mv1(mp, vs, i, 3-j, d)

dr = ['U','D','L','R']
rst = int(input())
st = input()
m = [st[i:i+4] for i in range(0, len(st), 4)]
ls = list(map(int, input().split()))
mp = [ls[i:i+4] for i in range(0, 16, 4)]
for i in m:
    a, b, c, d = i
    a = dr.index(a)
    b, c, d = int(b), int(c), int(d)
    mv(mp, a)
    mp[c][d] = b
print(rst)