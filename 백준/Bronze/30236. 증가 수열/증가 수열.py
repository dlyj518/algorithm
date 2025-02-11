t = int(input())
for i in range(t):
    n = int(input())
    an = list(map(int, input().split()))
    x = 0
    for i in range(n):
        while 1:
           x += 1
           if an[i] != x: break
    print(x)