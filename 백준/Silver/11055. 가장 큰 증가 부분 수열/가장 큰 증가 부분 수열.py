n = int(input())
ls = list(map(int, input().split()))
r = ls[:]
for i in range(n):
    for j in range(i):
        if ls[i] > ls[j]: r[i] = max(r[i], r[j]+ls[i])
print(max(r))