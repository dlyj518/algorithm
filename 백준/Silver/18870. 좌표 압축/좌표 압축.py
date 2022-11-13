import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int,input().split()))
srt = sorted(set(x))
dic = {srt[i]:i for i in range(len(srt))}
for a in x: print(dic[a], end=' ')