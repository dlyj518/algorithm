dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
n, k = map(int, input().split())
ls = list(input())
ln = list(range(n)) + list(range(n-2, -1, -1))
sm = [1]
for i in range(1, len(ln)): sm.append(sm[i-1] + ln[i] + 1)

y = x = 0
cnt = 1
for d in ls:
    y += dr[d][0]; x += dr[d][1]
    s = y + x
    if s < n: c = x
    else: c = x + n - s - 1
    if s % 2: ss = sm[s] - c
    else: ss = sm[s] - ln[s] + c
    cnt += ss
print(cnt)