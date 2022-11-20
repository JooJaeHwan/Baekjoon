'''
피보나치 수
https://www.acmicpc.net/problem/2747
재귀
'''


import sys

input = sys.stdin.readline

N = int(input())

a, b = 0, 1

for _ in range(N):
    a, b = b, a + b

print(a)