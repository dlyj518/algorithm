import bisect

def ms(x, n):
    xs = []
    for i in range(n):
        s = x[i]
        xs.append(s)
        for j in range(i + 1, n):
            s+=x[j]
            xs.append(s)
    xs.sort()
    return xs

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
sa, sb = ms(a, n), ms(b, m)
rs = 0
for i in range(len(sa)):
    l = bisect.bisect_left(sb, t - sa[i])
    r = bisect.bisect_right(sb, t - sa[i])
    rs += r - l
print(rs)