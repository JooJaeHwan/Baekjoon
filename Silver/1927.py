'''
최소 힙
https://www.acmicpc.net/problem/1927
자료 구조, 우선순위 큐
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if heap != []:
            print(heapq.heappop(heap))
        else: print(0)
    else:
        heapq.heappush(heap, num)
