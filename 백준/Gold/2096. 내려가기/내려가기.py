n = int(input())
mx, mn = [0]*3, [0]*3
xx, nn = [0]*3, [0]*3
for i in range(n):
    a, b, c = map(int, input().split())
    xx[0] = a + max(mx[:2])
    nn[0] = a + min(mn[:2])
    xx[1] = b + max(mx)
    nn[1] = b + min(mn)
    xx[2] = c + max(mx[1:])
    nn[2] = c + min(mn[1:])
    mx = xx[:]; mn = nn[:]
print(max(mx), min(mn))