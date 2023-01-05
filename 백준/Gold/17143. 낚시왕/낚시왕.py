import sys
input = sys.stdin.readline

def dcad(dc, x, y):
    if dc.get(x): dc[x].append(y)
    else: dc[x] = [y]

def dir(y, x, dd):
    d = dd % 2
    if 0 < y < x - 1: return (y, dd)
    x -= 1
    if y < 1:
        d = (y - 1) // x % 2
        yd = (y - 1) % x
        y = x - yd - 1 if d else yd + 1
    else:
        d = (y // x + 1) % 2
        yd = y % x
        y = yd if d else x - yd
    if dd > 1: d = 3 - d
    return (y, d)

r, c, m = map(int, input().split())
shk = {}
for i in range(m):
    a, b, s, d, z = map(int, input().split())
    a -= 1; b -= 1
    dcad(shk, (a, b), (s, d - 1, z, chr(i+65)))
rst = 0; dd = [-1, 1, 1, -1]

for i in range(c):
    nsk = {}
    for j in range(r):
        if shk.get((j, i), 0):
            rst += shk[(j, i)][0][2]
            del shk[(j, i)]
            break
    for y, x in shk:
        for s, d, z, a in shk[(y, x)]:
            if d < 2: y, d = dir(y + dd[d] * s, r, d)
            else: x, d = dir(x + dd[d] * s, c, d)
            dcad(nsk, (y, x), (s, d, z, a))
    # print(f'nsk: {nsk}')
    for y, x in nsk:
        if len(nsk[(y, x)]) > 1:
            sv = w = 0
            for j in range(len(nsk[(y, x)])):
                if w < nsk[(y, x)][j][2]: w = nsk[(y, x)][j][2]; sv = j
            nsk[(y, x)] = [nsk[(y, x)][sv]]
    shk = nsk
print(rst)