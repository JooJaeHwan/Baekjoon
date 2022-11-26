'''
DFS와 BFS
https://www.acmicpc.net/problem/1260
그래프 이론, 그래프 탐색, 넓이 우선 탐색, 깊이 우선 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]

def dfs(V):
    print(V, end=' ')
    visited[V] = True
    for i in adj[V]:
        if not(visited[i]):
            dfs(i)

def bfs(V):
    q = deque([V])
    while q:
        V = q.popleft()
        if not visited[V]:
            visited[V] = True
            print(V, end=' ')
            for i in adj[V]:
                if not visited[i]:
                    q.append(i)

for _ in range(M):
    X, Y = map(int, input().split())
    adj[X].append(Y)
    adj[Y].append(X)

for i in adj:
    i.sort()

visited = [False] * (N + 1) 
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)


