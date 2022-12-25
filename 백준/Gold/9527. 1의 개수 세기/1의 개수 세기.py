def f(x):
    bx = bin(x)[2:]
    l = len(bx) - 1
    r = 0
    for i in range(l, -1, -1):
        if bx[l-i] == '1':
            r += x - 2**i + 1 + ss[i]
            x -= 2**i
    return r

a, b = map(int, input().split())
ss = [0]
for i in range(1, 60): ss.append(2**(i - 1) + 2 * ss[i-1])
print(f(b) - f(a-1))