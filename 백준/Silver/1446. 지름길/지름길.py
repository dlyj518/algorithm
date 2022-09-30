n,d = map(int,input().split())
rt = [0] * (d+1)
sc = []
for _ in range(n):
    s,e,c = map(int,input().split())
    if e > d or c > e-s: continue
    sc.append([e,s,c])
for i in range(1,d+1):
    rt[i] = rt[i-1]+1
    for c in sc:
        if c[0] == i and rt[c[1]]+c[2] < rt[i]: rt[i] = rt[c[1]]+c[2]
print(rt[d])