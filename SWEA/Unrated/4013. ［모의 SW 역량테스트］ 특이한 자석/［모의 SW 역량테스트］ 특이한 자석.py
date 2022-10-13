from collections import deque

t = int(input())
for tc in range(1, t+1):
    rst = 0
    k = int(input())
    mg = [[]]
    for _ in range(4): mg.append(deque(list(map(int, input().split()))))
    for _ in range(k):
        m, s = map(int, input().split())
        q = deque([(m, s)])
        sp = [0]*5
        sp[m] = s
        while q:
            m, s = q.popleft()
            if m > 1 and mg[m][6] != mg[m-1][2] and not sp[m-1]: sp[m-1] = -s; q.append((m-1, -s))
            if m < 4 and mg[m][2] != mg[m+1][6] and not sp[m+1]: sp[m+1] = -s; q.append((m+1, -s))
        for i in range(1, 5): mg[i].rotate(sp[i])
    for i in range(4): rst += mg[i+1][0]*2**i
    print(f'#{tc} {rst}')