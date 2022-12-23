a = list(input())
b = list(input())
m = len(b)
x = [0]*m; y = x[:]
for i in range(len(a)):
    c = 0; l = ''
    for j in range(m):
        if c < x[j]: c = x[j]; l = y[j]
        elif a[i] == b[j]:
            x[j] = c+1; y[j] = l + b[j]
mx = max(x)
print(mx)
if mx: print(y[x.index(mx)])