n = int(input())
nm = list(map(int,input().split()))
x = [[0]*21 for _ in range(n-1)]
x[0][nm[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if x[i-1][j]:
            if j+nm[i] <= 20: x[i][j+nm[i]] += x[i-1][j]
            if j-nm[i] >= 0: x[i][j-nm[i]] += x[i-1][j]
print(x[-1][nm[-1]])