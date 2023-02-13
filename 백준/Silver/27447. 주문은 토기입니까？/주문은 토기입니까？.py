n, m = map(int, input().split())
ti = list(map(int, input().split()))
t = ti[0]
tt = t
c = x = y = i = 0
while y < n:
    if i == tt:
        if x > y:
            y += 1; i += 1
            if y == n: print('success'); break
            else: tt = ti[y]; continue
        else: print('fail'); break
    if not c: i += 1; c += 1; continue
    if i > t: print('fail'); break
    if i + m >= t:
        x += 1; c -= 1; i += 1
        if x >= n: continue
        t = ti[x]
    else: i += 1; c += 1