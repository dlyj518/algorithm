n = int(input())
a = [[] for _ in range(n+1)]
a[1] = list(map(int, input().split()))
b = [min(a[1][1:]), min(a[1][0], a[1][2]), min(a[1][:2])]
for i in range(2, n+1):
    a[i] = list(map(int, input().split()))
    for j in range(3): a[i][j] += b[j]
    b = [min(a[i][1:]), min(a[i][0], a[i][2]), min(a[i][:2])]
print(min(a[-1]))