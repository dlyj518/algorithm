x = 0
for a in input():
   x += 1
   if a == ':': x += 1
   if a == '_': x += 5
print(x)