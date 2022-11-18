'''
강의실
https://www.acmicpc.net/problem/1374
'''


import sys
import heapq

input = sys.stdin.readline


N = int(input())
lectures = []

for i in range(N):
    
    id, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))
    # 우선순위 큐를 이용해서 자동 정렬

heap = [] # 배정된 강의실

end = heapq.heappop(lectures)[1]
heapq.heappush(heap, end)

for _ in range(N - 1):
    new_start, new_end = heapq.heappop(lectures)
     
    end = heapq.heappop(heap)

    if new_start < end:
        heapq.heappush(heap, end)
        heapq.heappush(heap, new_end)
    else:
        heapq.heappush(heap, new_end)

print(len(heap)) 