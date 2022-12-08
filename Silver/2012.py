'''
등수 매기기
https://www.acmicpc.net/problem/2012
그리디 알고리즘, 정렬
'''


import sys

input = sys.stdin.readline

N = int(input())

array = []
result = 0
rank = 1


for _ in range(N):
    array.append(int(input()))

array.sort()

for i in array:
    result += abs(rank - i)
    rank += 1

print(result)

