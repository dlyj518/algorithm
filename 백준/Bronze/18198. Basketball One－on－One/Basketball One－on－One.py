x = input(); i = 0; n = len(x)
a = b = 0
while 1:
    if i == n: break
    if x[i] == 'A': a += int(x[i + 1])
    else: b += int(x[i + 1])
    i += 2
print('A') if a > b else print('B')