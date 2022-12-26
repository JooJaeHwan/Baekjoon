'''
결혼식
https://www.acmicpc.net/problem/5567
그래프 이론, 그래프 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    q = deque([x])

    while q:
        now = q.popleft()
        for x in graph[now]:
            if distance[x] == -1:
                distance[x] = distance[now] + 1
                q.append(x)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [-1] * (N + 1)
distance[1] = 0

bfs(1)

result = 0
for i in range(1, N + 1):
    if distance[i] != -1 and distance[i] <= 2:
        result += 1

print(result - 1)

        

