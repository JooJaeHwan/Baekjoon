'''
이분 그래프
https://www.acmicpc.net/problem/1707
그래프 이론, 그래프 탐색, 깊이 우선 탐색, 넓이 우선 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    visited[x] = 0
    while q:
        now = q.popleft()
        for y in graph[now]:
            if visited[y] == -1:
                visited[y] = (visited[now] + 1) % 2
                q.append(y)

def is_bipartite():
    for x in range(1, v+1):
        for y in graph[x]:
            if visited[x] == visited[y]:
                return False
    return True


T = int(input())

for _ in range(T):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [-1 for _ in range(v+1)]

    for i in range(1, v+1):
        if visited[i] == -1:
            bfs(i)
    if is_bipartite():
        print('YES')
    else:
        print('NO')
