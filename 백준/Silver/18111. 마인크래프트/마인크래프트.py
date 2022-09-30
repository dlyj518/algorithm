n,m,b = map(int,input().split())
gr = []
for _ in range(n): gr += map(int,input().split())
h, tm = 0, 100000000
dic = dict()
for a in gr: dic[a] = 1 if dic.get(a) == None else dic[a]+1
for k in range(min(gr), max(gr)+1):
    if sum(gr)+b >= k*m*n:
        ktm = 0
        for d in dic:
            dff = (d - k)*dic[d]
            ktm += dff*2 if dff > 0 else -dff
        if ktm <= tm: tm, h = ktm, k
print(tm, h)