x = [1] * 10001
for i in range(1, 10001):
    if x[i]: print(i)
    while x[i]:
        x[i] = 0
        y = i
        while i:
            y += i % 10
            i //= 10
        if y > 1e4: break
        i = y