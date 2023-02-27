n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
r = n
for i in a:
    if i > b: r += (i - b) // c + (1 if (i - b) % c else 0)
print(r)
