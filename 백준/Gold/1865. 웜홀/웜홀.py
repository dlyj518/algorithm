for _ in range(int(input())):
    n, m, w = map(int, input().split())
    gs = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        gs.append([s, e, t])
        gs.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        gs.append([s, e, -t])
    sr = [0]*2+[1e9]*(n-1)
    rst = 'NO'
    for a in range(n):
        for s, e, t in gs:
            if sr[e] > sr[s]+t:
                sr[e] = sr[s]+t
                if a == n-1: rst = 'YES'
    print(rst)