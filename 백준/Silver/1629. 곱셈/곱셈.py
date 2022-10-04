def nmj(y):
    if y == 1: return a % c
    aa = nmj(y//2)
    if y % 2 == 0: return aa * aa % c
    return aa * aa * a % c

a, b, c = map(int, input().split())
print(nmj(b))