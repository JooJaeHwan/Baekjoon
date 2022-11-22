'''
트로피 진열
https://www.acmicpc.net/problem/1668
구현
'''

import sys

input = sys.stdin.readline

high = 0
trophys = []
right_result = 0
left_result = 0
N = int(input())

for _ in range(N):
    trophys.append(int(input()))

for trophy in trophys:
    if trophy > high:
        right_result += 1
        high = trophy
high = 0
for trophy in trophys[::-1]:
    if trophy > high:
        left_result += 1
        high = trophy
print(right_result)
print(left_result)