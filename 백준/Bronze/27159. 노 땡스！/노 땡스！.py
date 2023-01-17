n = int(input())
ls = list(map(int, input().split()))
sm = b = 0
for x in ls:
    if x != b + 1: sm += x
    b = x
print(sm)