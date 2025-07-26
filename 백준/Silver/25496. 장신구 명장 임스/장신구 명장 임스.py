p, n = map(int, input().split())
ai = list(map(int, input().split()))

ai.sort()
c = 0
for a in ai:
    if p >= 200: break
    c += 1
    p += a
print(c)