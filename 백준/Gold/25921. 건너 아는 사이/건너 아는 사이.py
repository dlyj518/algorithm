n = int(input())
fr = [0] * (n + 1)
for i in range(2, n + 1):
    if not fr[i]:
        fr[i] = i
        for x in range(i * 2, n + 1, i):
            if not fr[x]: fr[x] = i
print(sum(fr))