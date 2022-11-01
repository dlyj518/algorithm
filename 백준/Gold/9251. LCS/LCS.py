a = list(input())
b = list(input())
m = len(b)
l = [0]*m
for i in range(len(a)):
    c = 0
    for j in range(m):
        if c < l[j]: c = l[j]
        elif a[i] == b[j]:
            l[j] = c+1
print(max(l))