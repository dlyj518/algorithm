t = int(input())
for _ in range(t):
    x, y, r, w, z, s = map(int, input().split())
    d = (w-x)**2 + (z-y)**2
    if (r-s)**2 < d < (r+s)**2: print(2)
    elif d == 0 and r == s: print(-1)
    elif (r+s)**2 == d or (r-s)**2 == d: print(1)
    else: print(0)