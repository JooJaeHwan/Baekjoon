'''
보석 도둑
https://www.acmicpc.net/problem/1202
자료구조, 그리디 알고리즘, 정렬, 우선순위 큐
'''


import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
bags = []

for _ in range(N):
    M, V = map(int, input().split())
    gems.append((M, V))

for _ in range(K):
    bags.append(int(input()))

gems.sort()
bags.sort()

heap = []
cur = 0
result = 0

for bag in bags:
    while cur < N:
        M, V = gems[cur]
        if bag >= M:
            heapq.heappush(heap, -V)
            cur += 1
        else:
            break
    
    if len(heap) > 0:
        V = -heapq.heappop(heap)
        result += V

print(result)