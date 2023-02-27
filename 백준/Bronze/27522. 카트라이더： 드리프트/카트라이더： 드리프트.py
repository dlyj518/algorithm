rk, rs = [], {'R': 0, 'B': 0}
for _ in range(8): rk.append(input().split())
rk.sort()
for i in range(8): rs[rk[i][1]] += 8 - i + (2 if i < 1 else 1 if i < 2 else 0)
if rs['R'] > rs['B']: print('Red')
else: print('Blue')