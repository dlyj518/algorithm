t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    a,b = [],[]
    i,rst = x,-1
    while i <= m*n:
        if (i-y) % n == 0: rst = i; break
        i += m
    print(rst)