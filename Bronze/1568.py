'''
새
https://www.acmicpc.net/problem/1568
수학, 구현
'''


import sys

input = sys.stdin.readline

N = int(input())

result = 0
K = 1

while N > 0:
    if N >= K:
        N -= K
        result += 1
        K += 1
    else:
        K = 1

print(result)
