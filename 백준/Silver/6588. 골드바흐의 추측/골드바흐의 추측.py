import sys
input = sys.stdin.readline

mx = 1000000
nm = [1] * (mx + 1)
for i in range(2, int(mx ** .5) + 1):
    if nm[i]:
        nm[i*2::i] = [0] * ((mx - i) // i)
while 1:
    n = int(input())
    if not n: break
    for i in range(3, n // 2 + 1, 2):
        if nm[i] and nm[n-i]: print(f'{n} = {i} + {n - i}'); break