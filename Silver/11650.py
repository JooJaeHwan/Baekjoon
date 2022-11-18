'''
좌표 정렬하기
https://www.acmicpc.net/problem/11650
정렬
'''


import sys

input = sys.stdin.readline

N = int(input())
result = []
for _ in range(N):
    x, y = map(int, input().split())
    result.append((x, y))

result.sort(key=lambda x: (x[0], x[1]))

for i in result:
    print(' '.join(map(str, i)))