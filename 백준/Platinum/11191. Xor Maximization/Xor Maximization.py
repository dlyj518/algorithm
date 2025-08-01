import math

n = int(input())
aa = list(map(int, input().split()))
bs = []
l = int(math.log2(max(aa)))
a = 0
for i in range(l, -1, -1):
    x = 1 if not (aa[a] & (1 << i)) else 0
    for j in range(a + 1, n):
        if aa[j] & (1 << i):
            if x: aa[a] ^= aa[j]; x = 0
            aa[j] ^= aa[a]
    if not x:
        bs.append(aa[a])
        a += 1
    if a >= n: break
x = 0
for b in bs:
    if not (x & (1 << (b.bit_length() - 1))):
        x ^= b
print(x)