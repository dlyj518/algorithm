h, m = map(int, input().split())
x = int(input())
(x, m) = (0, m + x) if m + x < 60 else divmod(m + x, 60)
h = h + x - 24 if h + x > 23 else h + x
print(h, m)