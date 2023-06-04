x = y = 0
for _ in range(int(input())):
    if input() == 'D': x += 1
    else: y += 1
    if abs(x - y) > 1: break
print(f'{x}:{y}')