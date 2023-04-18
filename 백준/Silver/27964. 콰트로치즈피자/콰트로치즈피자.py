n = int(input())
r = 0
s = set()
for x in input().split(): s.add(x)
for x in list(s):
    if x[-6:] == 'Cheese': r += 1
print('yummy') if r > 3 else print('sad')