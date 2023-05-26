n, a, b = map(int, input().split())
print('Bus') if a < max(n, b) else print('Subway') if a > max(n, b) else print('Anything')