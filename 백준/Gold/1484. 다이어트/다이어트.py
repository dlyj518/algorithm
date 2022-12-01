c = 0
g = int(input())
for i in range(int(g**.5), 0, -1):
    if g % i == 0 and ((g // i) - i) // 2 > 0 and (g // i + i) % 2 == 0: print((g // i + i) // 2); c += 1
if c == 0: print(-1)