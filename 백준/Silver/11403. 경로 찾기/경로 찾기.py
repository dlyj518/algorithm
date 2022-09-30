n = int(input())
eg = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if eg[i][j] or (eg[i][k] and eg[k][j]): eg[i][j] = 1
for i in range(n):
    for j in range(n): print(eg[i][j], end=' ')
    print()