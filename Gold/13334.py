'''
철로
https://www.acmicpc.net/problem/13334
자료구조, 정렬, 스위핑, 우선순위 큐
'''


import sys
import heapq

input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    start, end = map(int, input().split())

    if start > end:
        start, end = end, start
    lines.append((start, end))

lines.sort(key = lambda x: x[1])

d = int(input())

heap = []
cur = 0
result = 0
for line in lines:
    start, end = line

    if end - start > d:
        continue
    
    cur = end
    heapq.heappush(heap, start)
    while heap:
        start = heapq.heappop(heap)

        if cur - start > d:
            continue
        else:
            heapq.heappush(heap, start)
            break
    
    result = max(result, len(heap))

print(result)