import sys
input = sys.stdin.readline

def hs(x):
    mx = x
    while x != 1:
        if x % 2: x = x * 3 + 1; mx = max(x, mx)
        else: x //= 2
    return mx

for _ in range(int(input())): print(hs(int(input())))