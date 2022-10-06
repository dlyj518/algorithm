ls = [0]*31
for _ in range(28): ls[int(input())] = 1
i, x = 1, 0
while i < 31:
    if ls[i] == 0: print(i); x += 1
    if x == 2: break
    i += 1