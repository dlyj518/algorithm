n = int(input())
x = list(map(int, input().split()))
l = r = 0
mx = []
for i in x:
    if i == 1: l += 1; r -= 1
    else: l -= 1; r += 1
    mx.append(max(l, r))
    if l < 0: l = 0
    if r < 0: r = 0
print(max(mx))