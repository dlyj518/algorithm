t = int(input())
for tc in range(1, t+1):
    n, m, k, a, b = map(int, input().split())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    tt = [-1]+list(map(int, input().split()))
    tm = 0
    at, bt = [], []
    al, bl = [[0,0] for _ in range(n+1)], [[0,0] for _ in range(m+1)]
    aw, bw = set(), set()
    while 1:
        for i in range(1, k+1):
            if tt[i] == tm: at.append(i)
        for i in range(1, n+1):
            if al[i][1] == 1: bt.append(al[i][0]); al[i] = [0, 0]
            elif al[i][1] != 0: al[i][1] -= 1
            if al[i] == [0, 0] and at: al[i] = [at.pop(0), aa[i-1]]
        for j in range(1, m+1):
            if bl[j][1] == 1: bl[j] = [0, 0]
            elif bl[j][1] != 0: bl[j][1] -= 1
            if bl[j] == [0, 0] and bt: bl[j] = [bt.pop(0), bb[j-1]]
        aw.add(al[a][0]); bw.add(bl[b][0]);
        if tm >= max(tt) and not at and not bt and sum(sum(al,[])) == 0: break
        tm += 1
    rst = sum(aw & bw)
    rst = -1 if not rst else rst
    print(f'#{tc} {rst}')