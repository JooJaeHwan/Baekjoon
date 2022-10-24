'''
숫자의 개수
https://www.acmicpc.net/problem/2577
'''

import sys

input = sys.stdin.readline
answer = 1

for _ in range(3):
    answer *= int(input())

for i in range(10):
    print(str(answer).count(f'{i}'))