def mv(x, y):
    if x == 5: return 20 + y
    if x == 10:
        if y < 3: return 25 + y
        if y == 3: return 23
        return 24 + y
    if x == 23:
        if y > 4: return 0
        if y == 3: return 20
        return 27 + y
    if x <= 20 and x + y > 20: return 0
    return x + y

bd = {}
for i in range(4): bd[chr(i + 65)] = 0; bd[chr(i + 97)] = 0
db = [''] * 30
n = int(input())
for _ in range(n):
    a, b = input().split()
    mc = b.count('F')
    mc = mc if mc != 0 else 5
    tm = a.isupper()
    if bd[a]:
        c = bd[a]
        a = db[c]
        db[c] = ''
    for x in a:
        bd[x] = mv(bd[x], mc)
    if db[bd[x]] and db[bd[x]].isupper() != tm:
        for y in db[bd[x]]: bd[y] = 0
        db[bd[x]] = a
    else: db[bd[x]] += a
yb = ['..----..----..----..----..----..',
'..    ..    ..    ..    ..    ..',
'| \\                          / |',
'|  \\                        /  |',
'|   \\                      /   |',
'|    ..                  ..    |',
'..   ..                  ..   ..',
'..     \\                /     ..',
'|       \\              /       |',
'|        \\            /        |',
'|         ..        ..         |',
'|         ..        ..         |',
'..          \\      /          ..',
'..           \\    /           ..',
'|             \\  /             |',
'|              ..              |',
'|              ..              |',
'|             /  \\             |',
'..           /    \\           ..',
'..          /      \\          ..',
'|         ..        ..         |',
'|         ..        ..         |',
'|        /            \\        |',
'|       /              \\       |',
'..     /                \\     ..',
'..   ..                  ..   ..',
'|    ..                  ..    |',
'|   /                      \\   |',
'|  /                        \\  |',
'| /                          \\ |',
'..    ..    ..    ..    ..    ..',
'..----..----..----..----..----..']
ym = [[] for _ in range(4)]
for i in range(5): ym[0].append((24 - i * 6, 30))
for i in range(5): ym[0].append((0, 24 - i * 6))
for i in range(1, 6): ym[0].append((i * 6, 0))
for i in range(1, 6): ym[0].append((30, i * 6))
for i in range(1, 6): ym[0].append((5 * i, 30 - 5 * i))
for i in range(1, 3): ym[0].append((5 * i, 5 * i))
for i in range(2): ym[0].append((20 + 5 * i, 20 + 5 * i))
for x, y in ym[0]: ym[1].append((x, y + 1)); ym[2].append((x + 1, y)); ym[3].append((x + 1, y + 1))
for a in bd:
    if bd[a]:
        x = (ord(a) - 65) % 32
        i, j = ym[x][bd[a] - 1]
        yb[i] = yb[i][:j] + a + yb[i][j + 1:]
print(*yb, sep = '\n')