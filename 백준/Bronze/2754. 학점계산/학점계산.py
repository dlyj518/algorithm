x = {'+': .3, '0': .0, '-': -.3}
a = input()
print(0.0) if a == 'F' else print(69 - ord(a[0]) + x[a[1]])