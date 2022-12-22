n = int(input())
nm = [1]*(n+1)
pn = [2]
for j in range(4, n+1, 2): nm[j] = 0
for i in range(3, n+1, 2):
    if nm[i]:
        pn.append(i)
        for j in range(i*2, n+1, i): nm[j] = 0
rst = s = e = 0
while e <= len(pn):
    sm = sum(pn[s:e])
    if sm == n: rst += 1
    if sm < n: e += 1
    else: s += 1
print(rst)