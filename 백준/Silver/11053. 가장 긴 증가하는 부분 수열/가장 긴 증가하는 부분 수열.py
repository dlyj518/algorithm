n = int(input())
ls = list(map(int, input().split()))
r = []
for a in ls:
    for i in range(len(r)):
        if r[i] >= a: r[i] = a; break
    else: r.append(a)
print(len(r))