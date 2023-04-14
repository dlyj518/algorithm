s, t = input(), input()
ct = [0] * len(t)
if s[0] == t[0]: ct[0] = 1
for i in range(1, len(s)):
    j = 0
    while 1:
        if s[i] == t[j]:
            if j > 0: ct[j] = min(ct[j] + 1, ct[j - 1])
            else: ct[j] += 1
        if not ct[j] or j == len(t) - 1: break
        j += 1
print(ct[-1])