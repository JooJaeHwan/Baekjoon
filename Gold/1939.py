'''
중량제한
https://www.acmicpc.net/problem/1939
자료구조, 그래프 이론, 그래프 탐색, 이분 탐색, 너비 우선 탐색, 분리 집합
'''


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (N + 1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]


start = 1000000000
end = 1

for _ in range(M):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)