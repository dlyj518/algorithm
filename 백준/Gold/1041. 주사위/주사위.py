n = int(input())
ls = list(map(int, input().split()))
nls = [min(ls[0], ls[5]), min(ls[1], ls[4]), min(ls[2], ls[3])]
nls.sort()
if n == 1: print(sum(ls)-max(ls))
else: print(nls[2]*4 + nls[1]*8*(n-1) + nls[0]*(n*(5*n-8)+4))