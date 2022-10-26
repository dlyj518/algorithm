n = int(input())
ls = list(map(int, input().split()))
r = []
l = []
for a in ls:
    for i in range(len(r)):
        if r[i] >= a: l.append(i+1); r[i] = a; break
    else: r.append(a); l.append(len(r))
c = max(l)
print(c)
rs = []
for i in range(n-1, -1, -1):
        if l[i] == c: rs.append(ls[i]); c -= 1
print(*rs[::-1])