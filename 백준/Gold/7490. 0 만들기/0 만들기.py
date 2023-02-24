def bsum(a, b):
    if a > 0: return 10 * a + b
    return 10 * a - b

def chk(i, p, r, t):
    if i > n:
        if not r: print(t)
        return
    chk(i + 1, bsum(p, i), r - p + bsum(p, i), f'{t} {i}')
    chk(i + 1, i, r + i, f'{t}+{i}')
    chk(i + 1, -i, r - i, f'{t}-{i}')
for _ in range(int(input())):
    n = int(input())
    chk(2, 1, 1, '1')
    print()