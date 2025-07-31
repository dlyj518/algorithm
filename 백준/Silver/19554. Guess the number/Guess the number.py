n = int(input())
l, r = 1, n
while l <= r:
    m = (l +  r) // 2
    print(f'? {m}', flush=True)
    resp = int(input())
    if resp == 0: print(f'= {m}'); break
    if resp > 0: r = m - 1
    else: l = m + 1