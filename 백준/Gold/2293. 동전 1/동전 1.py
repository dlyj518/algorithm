n, k = map(int, input().split())
c = []
for _ in range(n): c.append(int(input()))

r = [0]*(k+1)
r[0] = 1
for i in c:
    for j in range(i, k+1):r[j] += r[j-i]
print(r[-1])