import sys
input = sys.stdin.readline

t, n = map(int, input().split())
lc = {str(i+1): '1' for i in range(n)}
bg = {str(i+1): {} for i in range(n)}
bj, bn = [], []

for tt in range(1, t+1):
    lg = list(input().split())
    if lg[2] == 'M': lc[lg[1]] = lg[3]
    if lg[2] == 'F':
        if lc[lg[1]] != lg[3]: bj.append(tt)
        if bg[lg[1]].get(lg[3], 0): bg[lg[1]][lg[3]] += 1
        else: bg[lg[1]][lg[3]] = 1
    if lg[2] == 'C':
        if bg[lg[1]].get(lg[3], 0): bg[lg[1]][lg[3]] -= 1
        else: bj.append(tt)
        if bg[lg[1]].get(lg[4], 0): bg[lg[1]][lg[4]] -= 1
        elif not bj or bj[-1] != tt: bj.append(tt)
    if lg[2] == 'A':
        if lc[lg[1]] != lc[lg[3]]: bj.append(tt); bn.append(int(lg[1]))
print(len(bj))
if len(bj): print(*bj)
bn = list(set(bn))
bn.sort()
print(len(bn))
if len(bn): print(*bn)