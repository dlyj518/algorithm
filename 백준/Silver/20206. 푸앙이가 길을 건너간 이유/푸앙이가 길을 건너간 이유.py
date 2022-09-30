a, b, c = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())
def xy(x, y): return a*x + b*y + c
if xy(x1, y1) * xy(x2, y2) < 0 or xy(x1, y2) * xy(x2, y1) < 0: print('Poor')
else: print('Lucky')