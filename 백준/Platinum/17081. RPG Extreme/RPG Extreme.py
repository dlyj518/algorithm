mv = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
n, m = map(int, input().split())
mp = []
k = l = 0
for i in range(n):
    mp.append(list(input()))
    for j in range(m):
        if mp[i][j] == '&': k += 1
        if mp[i][j] == 'B': l += 1
        if mp[i][j] == '@': sy, y, sx, x = i, i, j, j; mp[i][j] = '.'
cm = list(input())
ms, axi = {}, {}
for _ in range(k + 1):
    r, c, s, *ls = input().split()
    ms[int(r) - 1, int(c) - 1] = [s] + list(map(int, ls))
for _ in range(l):
    r, c, t, s = input().split()
    if t == 'W' or t == 'A': s = int(s)
    axi[int(r) - 1, int(c) - 1] = [t, s]
t, lv, ep, hp, at, df, mhp = 0, 1, 0, 20, 2, 2, 20
wp, am, ed = 0, 0, 0
ac, ax = 0, {'HR': 0, 'RE': 0, 'CO': 0, 'EX': 0, 'DX': 0, 'HU': 0, 'CU': 0}
for c in cm:
    t += 1
    ny, nx = y + mv[c][0], x + mv[c][1]
    if not (0 <= ny < n) or not (0 <= nx < m) or mp[ny][nx] == '#': ny, nx = y, x
    if mp[ny][nx] == '^': hp -= 1 if ax['DX'] else 5; nm = 'SPIKE TRAP'
    elif mp[ny][nx] == 'B':
        bb, bc = axi[ny, nx][0], axi[ny, nx][1]
        if bb == 'W': wp = bc
        elif bb == 'A': am = bc
        elif bb == 'O' and ac < 4 and not ax[bc]: ax[bc] = 1; ac += 1
        mp[ny][nx] = '.'
    elif mp[ny][nx] == '&' or mp[ny][nx] == 'M':
        if ax['HU'] and mp[ny][nx] == 'M': hp = mhp
        [nm, mw, ma, mh, me] = ms[ny, nx]
        att, dfs, fa = at + wp, df + am, 1
        if ax['CO']:
            if ax['DX']: ab = 3
            else: ab = 2
        else: ab = 1
        while mh > 0 and hp > 0:
            if fa: mh -= max(1, att * ab - ma)
            else: mh -= max(1, att - ma)
            if mh < 1: break
            if not fa or not (mp[ny][nx] == 'M' and ax['HU']): hp -= max(1, mw - dfs)
            fa = 0
        if hp > 0:
            if mp[ny][nx] == 'M': ed = 1
            mp[ny][nx] = '.'
            if ax['HR']: hp = min(hp + 3, mhp)
            ep += int(me * 1.2) if ax['EX'] else me
            if ep >= lv * 5: lv += 1; ep = 0; mhp += 5; hp = mhp; at += 2; df += 2
    if hp < 1 and ax['RE']: hp = mhp; y, x = sy, sx; ax['RE'] = 0; ac -= 1; continue
    y, x = ny, nx
    if hp < 1 or ed: break
if hp < 0: hp = 0
if hp: mp[y][x] = '@'
for i in range(n): print(*mp[i], sep='')
print(f'Passed Turns : {t}')
print(f'LV : {lv}')
print(f'HP : {hp}/{mhp}')
print(f'ATT : {at}+{wp}')
print(f'DEF : {df}+{am}')
print(f'EXP : {ep}/{lv * 5}')
if ed: print('YOU WIN!')
elif not hp: print(f'YOU HAVE BEEN KILLED BY {nm}..')
else: print('Press any key to continue.')