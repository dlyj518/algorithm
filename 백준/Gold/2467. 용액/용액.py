n = int(input())
ls = list(map(int, input().split()))
l = 0; r = n-1
ll = rr = 0
mn = 1e10
while l < r:
    sm = ls[l] + ls[r]
    if mn > abs(sm): ll = l; rr = r; mn = abs(sm)
    if sm > 0: r -= 1
    elif sm < 0: l += 1
    else: break
print(ls[ll], ls[rr])