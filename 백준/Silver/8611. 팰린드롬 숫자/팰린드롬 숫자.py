def jb(n, i):
    x = ''
    while n >= i:
        x = str(n % i) + x
        n //= i
    return str(n) + x
n = int(input())
a = 0
for i in range(2, 11):
    x = jb(n, i)
    if x == x[::-1]: print(f'{i} {x}'); a += 1
if not a: print('NIE')