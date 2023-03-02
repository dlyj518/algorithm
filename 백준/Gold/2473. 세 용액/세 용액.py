n = int(input())
ls = sorted(list(map(int, input().split())))
rs = []
mn = 1e10
for i in range(n - 2):
    x = ls[i]
    l, r = i + 1, n - 1
    while l < r:
        s = x + ls[l] + ls[r]
        if abs(s) <= mn:
            rs = [x, ls[l], ls[r]]
            mn = abs(s)
        if s < 0: l += 1
        elif s > 0: r -= 1
        else: break
    if not mn: break
print(*rs)