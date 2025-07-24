n, k = map(int, input().split())
tl = list(map(int, input().split()))

ar = []
for i in range(1, n):
    ar.append(tl[i] - tl[i - 1])
ar.sort(reverse=True)
print(sum(ar[k-1:]))