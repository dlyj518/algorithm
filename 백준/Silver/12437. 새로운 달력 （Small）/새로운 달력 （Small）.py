import sys, math
input = sys.stdin.readline

for i in range(int(input())):
    m, d, w = map(int, input().split())
    a = m - 1 - (m - 1) // (w // math.gcd(d%w, w)) + (m * d + w - 1) // w
    print(f'Case #{i + 1}: {a}')