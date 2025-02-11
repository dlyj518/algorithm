x = 0
n, c = map(int, input().split())
for i in range(n):
    tm = input()
    m, s = int(tm[0]), int(tm[2:])
    x += m * 60 + s
x -= c * (n - 1)
m, s = divmod(x, 60)
h, m = divmod(m, 60)
print(f'{h:02}:{m:02}:{s:02}')