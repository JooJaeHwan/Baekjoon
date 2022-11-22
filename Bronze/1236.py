'''
성 지키기
https://www.acmicpc.net/problem/1236
구현
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(str(input().strip()))
row = [0] * N
column = [0] * M

for i in range(N):
    for j in range(M):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1
row_count = 0
for i in range(N):
    if row[i] == 0:
        row_count += 1
column_count = 0
for i in range(M):
    if column[i] == 0:
        column_count += 1

print(max(row_count, column_count))

print(result)