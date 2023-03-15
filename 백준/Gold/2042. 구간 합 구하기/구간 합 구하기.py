import sys
input = sys.stdin.readline

def init(i, s, e):
    if s == e: tr[i] = ls[s]
    else:
        m = (s + e) // 2
        tr[i] = init(i * 2, s, m) + init(i * 2 + 1, m + 1, e)
    return tr[i]
def ss(i, s, e, l, r):
    if l > e or r < s: return 0
    if l <= s and r >= e: return tr[i]
    m = (s + e) // 2
    return ss(i * 2, s, m, l, r) + ss(i * 2 + 1, m + 1, e, l, r)
def ud(i, s, e, k, d):
    if k > e or k < s: return
    tr[i] += d
    if s != e:
        m = (s + e) // 2
        ud(i * 2, s, m, k, d)
        ud(i * 2 + 1, m + 1, e, k, d)

n, m, k = map(int, input().split())
ls, tr = [], [0] * 3000000
for _ in range(n): ls.append(int(input()))
init(1, 0, n - 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        df = c - ls[b - 1]
        ls[b - 1] = c
        ud(1, 1, n, b, df)
    else: print(ss(1, 1, n, b, c))