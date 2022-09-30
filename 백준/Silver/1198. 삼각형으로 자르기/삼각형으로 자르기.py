n = int(input())
ls = []
for _ in range(n): ls.append(list(map(int, input().split())))
rst = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x, y = ls[i]
            u, v = ls[j]
            w, z = ls[k]
            a, b = y - v, u - x
            c = -b*y - a*x
            s = abs(a*w + b*z + c) / 2
            rst.append(s)
print(max(rst))