for _ in range(int(input())):
    p = float(input())
    a, b = 1, 1
    while True:
        ab = round(a / b * 100 + 1e-9, 3)
        if b == 66672:
            print('if')
        if ab == p: print(b); break
        if ab > p: b += 1
        else: a += 1