'''
컵라면
https://www.acmicpc.net/problem/1781
자료구조, 그리디 알고리즘, 우선순위 큐
'''


import sys
import heapq

input = sys.stdin.readline

heap = []
array = []

N = int(input())

for _ in range(N):
    deadline, num = map(int, input().split())
    array.append((deadline, num))

array.sort()

for i in array:
    deadline = i[0]
    heapq.heappush(heap, i[1])
    if deadline < len(heap):
        heapq.heappop(heap)

print(sum(heap))

