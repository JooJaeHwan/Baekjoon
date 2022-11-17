'''
이중 우선순위 큐
https://www.acmicpc.net/problem/7662
'''


import sys
import heapq

input = sys.stdin.readline

T = int(input())

def pop(heap):
    while len(heap) > 0:
        data, id = heapq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    current = 0
    deleted = [False] * (k + 1)
    for _ in range(k):
        data = input().rstrip().split()
        if data[0] == 'I':
            heapq.heappush(min_heap, (int(data[1]), current))
            heapq.heappush(max_heap, (-int(data[1]), current))
            current += 1

        elif data[0] == 'D':
            if data[1] == '-1':pop(min_heap)
            elif data[1] == '1':pop(max_heap)
    max_value = pop(max_heap)
    if max_value == None:
        print("EMPTY")
    else:
        heapq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))