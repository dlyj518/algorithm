n = int(input())
s = n
for i in range(1, n):
    if not n % i: s += i
print(s * 5 - 24)