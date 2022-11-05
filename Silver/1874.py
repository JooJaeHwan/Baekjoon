'''
스택 수열
https://www.acmicpc.net/problem/1874
'''

import sys

input = sys.stdin.readline

N = int(input())
cnt = 1
stack = []
result = []

for _ in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break

else: print('\n'.join(result))