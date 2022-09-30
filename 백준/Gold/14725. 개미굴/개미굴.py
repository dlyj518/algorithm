n = int(input())
ls = []
num = []
for _ in range(n):
    inp = list(input().split())
    ls.append(inp[1:])
    num.append(int(inp[0]))
mx = max(num)
ls.sort()
rst = [[] for _ in range(mx)]
for a in ls:
    aa = ''
    for i in range(len(a)):
        aa += '.'+a[i]
        if aa in rst[i]: continue
        rst[i].append(aa)
        print((2*i)*'-'+a[i])