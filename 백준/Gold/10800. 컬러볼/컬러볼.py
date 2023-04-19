import sys
input = sys.stdin.readline

n = int(input())
ls = []
rs = [0] * n
for i in range(n): ls.append(list(map(int, input().split())) + [i])
ls.sort(key=lambda x: (x[1], x[0]))
c, s = [0] * (n + 1), 0
j = 0
for i in range(n):
    a, b = ls[i], ls[j]
    while b[1] < a[1]:
        s += b[1]
        c[b[0]] += b[1]
        j += 1; b = ls[j]
    rs[a[2]] = s - c[a[0]]
for x in rs: print(x)