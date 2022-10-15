import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
from pprint import pprint
from math import gcd
import heapq

from itertools import combinations
from copy import deepcopy

dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
bl = [[], [2, 0, 3, 1], [3, 2, 0, 1], [1, 3, 0, 2], [2, 3, 1, 0]]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    wh = {6:[], 7:[], 8:[], 9:[], 10:[]}
    mp = []
    for i in range(n):
        mp.append(list(map(int, input().split())))
        for j in range(n):
            if mp[i][j] == -1: y, x = i, j
            if mp[i][j] > 5: wh[mp[i][j]].append([i,j])
    for d in range(4):
        c = 0
        mmp = deepcopy(mp)
        while 1:
            y += dy[d]; x += dx[d]
            if not (0<=y<n) or not (0<=x<n) or mmp[y][x] == 5: break
            if 0 < mmp[y][x] < 5: d = bl[mmp[y][x]][d]
            if mmp[y][x] > 5: continue
            c += 1

