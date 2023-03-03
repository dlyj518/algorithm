n = int(input())
ls = [0] + list(map(int, input().split()))
x = ls[:]
rs, c = [], 0
for i in range(1, n + 1):
    if i != x[i]:
        c += 1; y = x.index(i)
        m = (y - i) // 2 + 1
        rs.append(f'{i} {y}')
        for j in range(m): x[i + j], x[y - j] = x[y - j], x[i + j]
if c < 3:
    for a in rs: print(a)
    for i in range(2 - c): print('1 1')
    quit()
rs, c = [], 0
for i in range(n, 0, -1):
    if i != ls[i]:
        c += 1; y = ls.index(i)
        m = (i - y) // 2 + 1
        rs.append(f'{y} {i}')
        for j in range(m): ls[i - j], ls[y + j] = ls[y + j], ls[i - j]
for a in rs: print(a)
for i in range(2 - c): print('1 1')