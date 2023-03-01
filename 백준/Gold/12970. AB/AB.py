n, k = map(int, input().split())
if not k: print('A' * n); quit()
for i in range(1, n // 2 + 1):
    if k <= i * (n - i): a, b = i, n - i; break
else: print(-1); quit()
p = ['B'] * n
x, y = k // b, k % b
p[:x] = ['A'] * x
if y: p[-y - 1] = 'A'
print(''.join(p))