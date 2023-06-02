n = int(input())
s = sum(map(int, input().split()))
t = (n - 1) * 8
print((s + t) // 24, (s + t) % 24)