'''
소수의 곱
https://www.acmicpc.net/problem/2014
'''


import sys
import heapq

input = sys.stdin.readline

K, N = map(int, input().split())

data = list(map(int, input().split()))

heap = []
visited = set()
max_value = max(data)

for x in data:
    heapq.heappush(heap, x)

for i in range(N - 1):
    element = heapq.heappop(heap)
    for x in data:
        now = element * x
        if len(heap) >= N and max_value < now:
            continue
        if now not in visited:
            heapq.heappush(heap, now)
            max_value = max(max_value, now)
            visited.add(now)

print(heapq.heappop(heap))
