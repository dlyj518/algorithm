import sys
input = sys.stdin.readline

def rnd(x): return int(x) if x % 1  < .5 else int(x + 1)

n = int(input())
df = []
for _ in range(n): df.append(int(input()))
df.sort()
j = rnd(n * 0.15)
dd = sum(df[j:-j] if j else df)
print(rnd((dd) / (n - j * 2))) if n else print(0)