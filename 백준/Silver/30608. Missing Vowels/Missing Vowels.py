s = input().strip()
f = input().strip()

s = s.lower()
f = f.lower()

vw = {'a', 'e', 'i', 'o', 'u', 'y'}

i = 0
c = 0

for j in range(len(f)):
    if s[i] == f[j]:
        c += 1
        i += 1
        if i == len(s): break
    elif not (f[j] in vw): break
for k in range(j + 1, len(f)):
    if not (f[k] in vw): print('Different'); break
else:
    if c == len(s): print('Same')
    else: print('Different')