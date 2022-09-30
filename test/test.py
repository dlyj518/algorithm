import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
from pprint import pprint
from math import gcd
import heapq

n = int(input())
mp = []
fs = [0]*7
sl, exp = 2, 0
for i in range(n):
    mp.append(list(map(int,input().split())))
    for j in range(n):
        if mp[i][j] == 9: sk = deque([(i, j)])
        elif mp[i][j] != 0: fs[mp[i][j]] += 1
while 1:
    