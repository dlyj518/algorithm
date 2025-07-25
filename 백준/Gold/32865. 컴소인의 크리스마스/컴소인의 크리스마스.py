n = int(input())
p = 0
cnt = {}
ans = [0] * (n * 2 - 1)
for i in range(n):
    x = int(input())
    p += x
    if cnt.get(x, 0): cnt[x].append(i + 1)
    else: cnt[x] = [i + 1]

od, ev = 0, 1
srt = sorted(cnt.items())

if p != n - 1: print(-1)
else:
    for a in srt[0][1]:
        ans[od] = a
        od += 2
    for i in range(1, len(srt)):
        for a in srt[i][1]:
            for j in range(srt[i][0]):
                ans[ev] = a
                ev += 2
            ans[od] = a
            od += 2
    for i in ans: print(i)