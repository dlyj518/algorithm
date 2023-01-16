def mx(x): global sm; sm = max(sm, x)

yn = list(input())
for i in range(12): yn[i] = 1 if yn[i] == 'Y' else 0
dc = sorted(list(map(int, input().split())))
sm = 0
if yn[10] and dc[0] == dc[2]: sm = 50
elif len(set(dc)) > 2 and ((dc[0] != 1 and yn[9]) or (dc[2] != 6 and yn[8])): sm = 30
elif yn[11]: sm = sum(dc) + 12
else:
    if len(set(dc)) < 3 and yn[7]:
        if dc[0] == dc[2]:
            if dc[0] == 6: mx(28)
            else: mx(sum(dc) + 12)
        elif dc[2] > dc[1]: mx(sum(dc) + dc[2] * 2) 
        else: mx(sum(dc) + dc[2] + dc[0])
    if len(set(dc)) < 3  and yn[6]: mx(4 * dc[0]) if dc[0] == dc[1] else mx(4 * dc[2])
    for i in range(1, 7):
        if yn[i - 1]: mx(i * (dc.count(i) + 2))
print(sm)