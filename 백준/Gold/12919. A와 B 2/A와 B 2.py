s, t = input(), input()
def df(x):
    if x == s: return 1
    if not len(x): return 0
    if x[-1] == 'A' and df(x[:-1]): return 1
    if x[0] == 'B' and df(x[1:][::-1]): return 1
    return 0
print(df(t))