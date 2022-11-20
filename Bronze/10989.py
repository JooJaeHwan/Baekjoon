'''
수 정렬하기 3
https://www.acmicpc.net/problem/10989
정렬
'''


import sys

input = sys.stdin.readline

N = int(input())
result = [0] * 10001

for _ in range(N):
    num = int(input())
    result[num] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)