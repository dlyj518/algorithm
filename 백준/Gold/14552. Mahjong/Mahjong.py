def chkpae(pp, h=0, b=0, i=1):
    pae = pp[:]
    if h == 1 and b == 4: return True
    while i < 10:
        if pae[i] > 0:
            if pae[i] >= 3 and b < 4:
                pae[i] -= 3; rst = chkpae(pae, h, b+1, i)
                if rst: return True
                pae[i] += 3
            if pae[i] >= 2 and not h:
                pae[i] -= 2; rst = chkpae(pae, h+1, b, i)
                if rst: return True
                pae[i] += 2
            if i < 8 and pae[i+1] and pae[i+2]:
                pae[i] -= 1; pae[i+1] -= 1; pae[i+2] -= 1
                rst = chkpae(pae, h, b+1, i)
                if rst: return True
            return False
        else: i += 1


ls = list(map(int, input().split()))
pae = [0]*10
for i in ls:
    pae[i] += 1
rst = []
for i in range(1, 10):
    if pae[i] == 4: continue
    pp = pae[:]
    pp[i] += 1
    p7 = 0
    for j in range(1, 10):
        if pp[j] == 2: p7 += 1
    if p7 == 7: rst.append(i)
    elif chkpae(pp): rst.append(i)
if rst: print(*rst)
else: print(-1)