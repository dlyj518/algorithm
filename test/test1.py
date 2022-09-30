import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline
from pprint import pprint
from math import gcd
import heapq

ldd = {1 : 2}
bmd = {99 : 1}
i = 101
while i < 102:
    mn = 1
    if i in ldd: print(1)
    if i in bmd: print(2)
    i += 1