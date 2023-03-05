def bt(x, n):
    if not n: return 1
    s = list(set([x % 10 ** n, x // 10]))
    rs = 0
    for i in s: rs += bt(i, n - 1)
    return rs

x = input()
n, x = len(x), int(x)
print(bt(x, n - 1))