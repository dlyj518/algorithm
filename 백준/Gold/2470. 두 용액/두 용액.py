n = int(input())
ls = list(map(int, input().split()))
ls.sort()
l, r = 0, n - 1
aw = 2e9 + 1
rs = []
while l < r:
    sl, sr = ls[l], ls[r]
    ss = sl + sr
    if abs(ss) < aw: aw = abs(ss); rs = [sl, sr]
    if not ss: break
    if ss < 0: l += 1
    else: r -= 1
print(*rs)