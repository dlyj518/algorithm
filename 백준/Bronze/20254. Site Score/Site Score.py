r = 0
for i, j in zip([56, 24, 14, 6], map(int, input().split())): r += i * j
print(r)