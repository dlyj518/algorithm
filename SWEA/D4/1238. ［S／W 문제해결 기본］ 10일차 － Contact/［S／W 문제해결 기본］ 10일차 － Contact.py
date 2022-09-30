for t in range(1, 11):
    l, s = map(int,input().split())
    ft = [[] for _ in range(101)]
    vs = [0]*101
    frto = list(map(int,input().split()))
    for i in range(l//2):
        ft[frto[i*2]].append(frto[i*2+1])
    n = 1
    vs[s] = 1
    q = [(s, n+1)]
    while q:
        x, n = q.pop(0)
        for a in ft[x]:
            if vs[a] == 0: vs[a] = n; q.append((a, n+1))
    rst = 100 - vs[::-1].index(max(vs))
    print(f'#{t} {rst}')