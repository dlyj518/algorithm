xx = list(map(int,input().split()))
n = min(xx)
while 1:
    cnt = 0
    for i in xx:
        if n % i == 0:
            cnt += 1
    if cnt >= 3: print(n); break
    n += 1