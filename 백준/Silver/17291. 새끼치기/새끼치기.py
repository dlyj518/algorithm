n = int(input())
l = [0, 1]
for i in range(2, n+1):
    mn = max(0, (i + 1) // 2 * 2 - 4)
    l.append(sum(l[mn:]))
yr = max(0, n // 2 * 2 - 2)
print(sum(l[yr:]))