import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
from pprint import pprint
from math import gcd
import heapq

from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    n, m, k, a, b = map(int, input().split())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    tt = list(map(int, input().split()))
    t = 0
    at, bt = 0, 0
    al, bl = [0]*n, [0]*m
    while 1:
        at += tt.count(t)
        for i in range(n):
            if not al[i]
