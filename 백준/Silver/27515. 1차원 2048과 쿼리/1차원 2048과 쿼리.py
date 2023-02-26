import sys
input = sys.stdin.readline
from math import log2

ls = [0] * 63
for _ in range(int(input())):
    x = input()
    if x[1] == '0': pass
    elif x[0] == '+': ls[int(log2(int(x[1:])))] += 1
    else: ls[int(log2(int(x[1:])))] -= 1
    c = 0
    mx = -1
    for i in range(63):
        if ls[i] + c: c = (ls[i] + c) // 2; mx = i
        else: c = 0
    print(2 ** mx) if mx >= 0 else print(0)