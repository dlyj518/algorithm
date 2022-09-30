n, k = map(int, input().split())
l, cnt = [], 0
for _ in range(n): l.append(int(input()))
while n > 0:
    d, k = divmod(k, l[n-1])
    cnt += d
    n -= 1
print(cnt)