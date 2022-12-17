n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    b = list(map(int, input().split()))
    for j in range(m): a[i][j] += b[j]
    print(*a[i])