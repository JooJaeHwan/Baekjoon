'''
별 찍기 - 2
https://www.acmicpc.net/problem/2439
'''

import sys

input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)