'''
검증수
https://www.acmicpc.net/problem/2475
'''

import sys

input = sys.stdin.readline

data = list(map(int, input().split()))
answer = sum([d**2 for d in data])

print(answer % 10)