'''
문제집
https://www.acmicpc.net/problem/1766
자료 구조, 그래프 이론, 우선순위 큐, 위상 정렬
'''


import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

problem_list = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

heap = []
result = []

for _ in range(M):
    A, B = map(int, input().split())
    problem_list[A].append(B)
    indegree[B] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for j in problem_list[temp]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(heap, j)

print(" ".join(map(str, result)))
