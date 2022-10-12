n = int(input())
tr = [[0]*(n+1) for _ in range(n)]
tr[0][1] = int(input())
for i in range(1,n):
    tr[i][1 : i+1] = map(int, input().split())
    for j in range(i+1):
        tr[i][j+1] += max(tr[i-1][j], tr[i-1][j+1])
print(max(tr[-1]))