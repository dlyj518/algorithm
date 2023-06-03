x = list(input())
for a in list('MOBIS'):
    for b in x:
        if a == b: break
    else: print('NO'); break
else: print('YES')