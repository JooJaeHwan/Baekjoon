'''
절댓값 힙
https://www.acmicpc.net/problem/11286
'''


import sys
import heapq


input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            absolute, real = heapq.heappop(heap)
            print(real)
    else:
        heapq.heappush(heap, (abs(x), x))