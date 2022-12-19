pt = []
for _ in range(3): pt.append(list(map(int, input().split())))
v1 = [pt[1][0] - pt[0][0], pt[1][1] - pt[0][1]]
v2 = [pt[2][0] - pt[1][0], pt[2][1] - pt[1][1]]
cp = (v1[0] * v2[1] - v1[1] * v2[0])
if cp: print(cp//abs(cp))
else: print(0)