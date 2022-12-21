import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def fnd(x):
    if x == pr[x]: return x
    pr[x] = fnd(pr[x])
    return pr[x]

pr = [i for i in range(int(input()) + 1)]
rst = 0
for _ in range(int(input())):
    i = fnd(int(input()))
    if not i: break
    pr[i] = i - 1
    rst += 1
print(rst)