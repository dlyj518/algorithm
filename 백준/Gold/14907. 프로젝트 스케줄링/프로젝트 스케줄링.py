pr = [[] for _ in range(26)]
sn = [0] * 26
tm = [0] * 26
rs = [0] * 26

while 1:
    try:
        a, *x = input().split()
        a = ord(a) - 65
        tm[a] = int(x[0])
        if len(x) > 1:
            for b in x[1]:
                y = ord(b) - 65
                pr[y].append(a)
                sn[a] += 1
    except: break

q = []
for i in range(26):
    if not sn[i] and tm[i]: q.append(i)
while q:
    x = q.pop()
    rs[x] += tm[x]
    for i in pr[x]:
        rs[i] = max(rs[i], rs[x])
        sn[i] -= 1
        if not sn[i]: q.append(i)
print(max(rs))