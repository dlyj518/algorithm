n = int(input())
b = list(map(int, input().split()))
d = int(input())
s = b.count(1)
if s > 2: print('NO'); quit()
for i in range(n - d + 1):
    if not b[i] or b[i] == 2: continue
    x = s
    if b[i] == 1:
        if b[i + d] == 1: x -= 2
        elif b[i + d]: x -= 1
    elif b[i]:
        if b[i + d] == 1: x -= 1
        if not b[i + d]: x += 1
    if not x: print('YES'); print(i, i + d); break
else: print('NO')