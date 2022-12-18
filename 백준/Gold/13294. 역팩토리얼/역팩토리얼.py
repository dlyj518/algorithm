from math import log, pi, factorial
n = int(input())
if log(n, 10) < 19:
    f = 1
    for i in range(1, 21):
        f *= i
        if f == n: print(i)
else:
    ln = log(n)
    x = 20
    while 1:
        lf = x * (log(x) - 1) + log(2 * pi * x) / 2
        if abs(ln - lf) < 1: print(x); break
        x += 1