a = [0]
s = {0}
x = 0

for i in range(1, int(input()) + 1):
    x = a[-1] - i
    if (x < 0) or (x in s): x = a[-1] + i
    a.append(x)
    s.add(x)
print(x)