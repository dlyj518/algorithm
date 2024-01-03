n, s, r = map(int, input().split())
s = sorted(list(map(int, input().split())))
r = list(map(int, input().split()))
x = 0
for i in r:
    if i in s: r.remove(i); s.remove(i)
for i in s:
    if i in r: r.remove(i)
    elif i - 1 in r: r.remove(i - 1)
    elif i + 1 in r: r.remove(i + 1)
    else: x += 1
print(x)