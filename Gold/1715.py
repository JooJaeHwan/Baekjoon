'''
카드 정렬하기
https://www.acmicpc.net/problem/1715
자료 구조, 그리디 알고리즘, 우선순위 큐
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
result = 0
for _ in range(N):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    value = one + two
    result += value
    heapq.heappush(heap, value)

print(result)