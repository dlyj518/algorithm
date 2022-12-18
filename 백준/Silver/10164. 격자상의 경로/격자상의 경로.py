from math import factorial as ft

n, m, k = map(int, input().split())
def p(a, b): return ft(a+b)//(ft(a)*ft(b))
if k:
    a, b = (k-1) // m, k % m if k % m else m
    print(p(a, b-1) * p(n-a-1, m-b))
else: print(p(n-1, m-1))