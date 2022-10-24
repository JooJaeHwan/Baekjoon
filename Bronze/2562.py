'''
최댓값
https://www.acmicpc.net/problem/2562
'''

import sys

input = sys.stdin.readline
data = []

for _ in range(9):
    data.append(list(map(int, input().split())))

print(max(data)[0])
print(data.index(max(data)) + 1)