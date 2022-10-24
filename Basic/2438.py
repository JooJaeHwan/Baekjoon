'''
별 찍기 - 1
https://www.acmicpc.net/problem/2438
'''

import sys

input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    print('*'*i)