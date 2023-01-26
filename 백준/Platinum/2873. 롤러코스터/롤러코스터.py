def hsp(y, x):
    by = y // 2 * 2
    rs = sp(by, c, ['R', 'L'], 'D')
    if rs != '': rs += 'D'
    bx = x // 2
    rs += 'DRUR' * bx
    rs += 'DR' if x % 2 else 'RD'
    rs += 'RURD' * (c // 2 - bx - 1)
    if r > by + 2: rs += 'D'
    rs += sp(r - by - 2, c, ['L', 'R'], 'D')
    print(rs)

def sp(r, c, f, s):
    rs = ''
    for i in range(1, r * c):
        if not i % c: rs += s
        elif (i // c) % 2: rs += f[1]
        else: rs += f[0]
    return rs

def psp(x): print(x)

r, c = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(r)]
rs = ''
if (r * c) % 2:
    psp(sp(r, c, ['R', 'L'], 'D'))
elif (r + c) % 2:
    if r % 2: psp(sp(r, c, ['R', 'L'], 'D'))
    else: psp(sp(c, r, ['D', 'U'], 'R'))
else:
    mn, mx, my = 1000, 0, 0
    for i in range(r):
        for j in range(1, c, 2):
            if i % 2: j -= 1
            if mp[i][j] < mn: mn, my, mx = mp[i][j], i, j
    hsp(my, mx)