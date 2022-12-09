n = int(input())
lg = {}
for _ in range(n):
    l, m = input().split()
    if m == 'enter': lg[l] = 1
    else: lg[l] = 0
lg = sorted(lg.items(), reverse=True, key=lambda x:x[0])
for i, j in lg:
    if j: print(i)