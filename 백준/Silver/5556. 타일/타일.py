from math import ceil
def chg(x):
    y = ceil(n / 2)
    return x if x < y else n - x + 1
def cal(x): return (x - 1) % 3 + 1

n = int(input())
k = int(input())
for _ in range(k):
    a, b = map(chg, map(int, input().split()))
    print(cal(a)) if a < b else print(cal(b))