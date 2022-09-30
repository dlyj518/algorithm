t = int(input())
for _ in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n):
        a,b = input().split()
        if dic.get(b) == None: dic[b] = 1
        else: dic[b] += 1
    x = list(dic.values())
    z = 1
    for i in x:
        z *= i+1
    print(z-1)