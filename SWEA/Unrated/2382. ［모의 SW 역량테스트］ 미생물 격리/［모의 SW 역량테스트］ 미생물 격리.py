dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    ms = []
    for _ in range(k): ms.append(list(map(int, input().split())))
    for _ in range(m):
        dc = {}
        for i in range(len(ms)):
            ms[i][0] += dy[ms[i][3]];ms[i][1] += dx[ms[i][3]]
            if dc.get((ms[i][0], ms[i][1]), 0): dc[(ms[i][0], ms[i][1])].append(ms[i])
            else: dc[(ms[i][0], ms[i][1])] = [ms[i]]
        ms = []
        for d in dc:
            if len(dc[d]) > 1:
                mix = sorted(dc[d], key = lambda x: x[2])
                ms.append([mix[0][0], mix[0][1], sum([mix[ii][2] for ii in range(len(mix))]), mix[-1][3]])
            else:
                if not(0 < dc[d][0][0] < n-1) or not(0 < dc[d][0][1] < n-1): ms.append([dc[d][0][0], dc[d][0][1], dc[d][0][2]//2, (dc[d][0][3]+1)//2*2 - (dc[d][0][3]+1)%2])
                else: ms.append(dc[d][0])
    rst = sum([ms[i][2] for i in range(len(ms))])
    print(f'#{tc} {rst}')