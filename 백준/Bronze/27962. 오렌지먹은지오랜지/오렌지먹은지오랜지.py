def chk(a, b, m):
    r = 0
    for i in range(m):
        if a[i] != b[i]: r += 1
    if r == 1: return 1
    return 0

n = int(input())
s = list(input())
for i in range(1, n):
    a, b = s[:i], s[-i:]
    if chk(a, b, i): print('YES'); break
else: print('NO')