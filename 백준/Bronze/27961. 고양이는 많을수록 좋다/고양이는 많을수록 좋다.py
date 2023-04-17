from math import log2, ceil
x = int(input())
print(ceil(log2(x)) + 1) if x > 0 else print(0)