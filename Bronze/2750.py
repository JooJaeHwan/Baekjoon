'''
수 정렬하기
https://www.acmicpc.net/problem/2750
정렬
'''

import sys

input = sys.stdin.readline

N = int(input())
result = []

for _ in range(N):
    num = int(input())
    result.append(num)
for i in range(N):
    for j in range(N):
        if result[i] < result[j]:
            result[i], result[j] = result[j], result[i]
print('\n'.join(map(str, result)))