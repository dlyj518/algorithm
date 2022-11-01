k,n = map(int,input().split())
r = [int(input()) for _ in range(k)]
s,e = 1, max(r)
while s <= e:
    m = (s+e)//2
    l = 0
    for a in r: l += a//m
    if l >= n: s = m+1
    else: e = m-1
print(e)