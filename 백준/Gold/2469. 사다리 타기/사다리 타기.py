k, n = int(input()), int(input())
st = list(map(chr, range(65, 65 + k)))
rs = list(input())
ld = [list(input()) for _ in range(n)]
for i in range(n -1, -1, -1):
    if ld[i][0] == '?': break
    for j in range(k - 1):
        if ld[i][j] == '-': rs[j], rs[j + 1] = rs[j + 1], rs[j]
for i in range(n):
    if ld[i][0] == '?': break
    for j in range(k - 1):
        if ld[i][j] == '-': st[j], st[j + 1] = st[j + 1], st[j]
r = ''
for i in range(k - 1):
    if st[i] == rs[i] or (r and r[-1] == '-'): r += '*'
    elif st[i] == rs[i + 1]: r += '-'
    else: r = 'x' * (k - 1); break
print(r)