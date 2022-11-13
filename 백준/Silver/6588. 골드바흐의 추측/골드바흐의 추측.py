mx = 1000001
nm = [1] * mx
nm[0:2] = [0] * 3
for i in range(4, mx, 2): nm[i] = 0
for i in range(3, 1001, 2):
    if nm[i]:
        for j in range(i * 2, mx, i): nm[j] = 0
while 1:
    n = int(input())
    if not n: break
    for i in range(3, n//2+1, 2):
        if nm[i] and nm[n-i]: print(n, '=', i, '+', n-i); break