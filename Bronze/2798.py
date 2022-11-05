'''
블랙잭
https://www.acmicpc.net/problem/2798
'''

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

number = (list(map(int, input().split())))

tmp = 0

for a in list(combinations(number, 3)):
    if sum(a) <= M :
        tmp = max(sum(a), tmp)

print(tmp)
