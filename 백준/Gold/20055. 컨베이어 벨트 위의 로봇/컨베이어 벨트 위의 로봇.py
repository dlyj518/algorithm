from collections import deque

n,k = map(int, input().split())
a = deque(list(map(int, input().split())))
rb = deque([0]*n)
cnt = 0
while 1:
    cnt += 1
    a.rotate(); rb.rotate()
    rb[-1] = 0
    if 1 in rb:
        for i in range(n-1, 0, -1):
            if rb[i-1] and not rb[i] and a[i] > 0:
                a[i] -= 1
                rb[i-1], rb[i] = 0, 1
    rb[-1] = 0
    if not rb[0] and a[0] > 0: a[0] -= 1; rb[0] = 1
    if a.count(0) >= k: break
print(cnt)