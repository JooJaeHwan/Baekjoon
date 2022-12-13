'''
선 긋기
https://www.acmicpc.net/problem/2170
정렬, 스위핑
'''


import sys

input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    x, y = map(int, input().split())
    array.append((x, y))
array.sort()

start, end = array[0]
result = 0
for x, y in array:
    if x <= end:
        end = max(end, y)
    else:
        result += end - start
        start = x
        end = y
result += end - start
print(result)