from math import ceil
x = int(input()); a = int(input()); b = int(input()); c = int(input()); d = int(input())
print(x - max(ceil(a / c), ceil(b / d)))