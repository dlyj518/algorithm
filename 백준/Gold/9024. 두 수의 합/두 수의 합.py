for t in range(int(input())):
    n, k = map(int, input().split())
    ls = sorted(list(map(int, input().split())))
    a, c = 2 * 10 ** 8, 0
    l, r = 0, n - 1
    while l < r:
        s = ls[l] + ls[r]
        if s == k: l += 1; r -= 1
        elif s > k: r -= 1
        else: l += 1
        if abs(k - s) < a: c = 1; a = abs(k - s)
        elif abs(k - s) == a: c += 1
    print(c)