a, b = map(int, input().split())
c, d = map(int, input().split())
b *= 1.01; d *= 1.01
if a + d > b + c: print('Persepolis')
elif a + d < b + c: print('Esteghlal')
else: print('Penalty')