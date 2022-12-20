'''
노드사이의 거리
https://www.acmicpc.net/problem/1240
그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 넓이 우선 탐색
'''


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    for data in graph[x]:
        y = data[0]
        cost = data[1]
        if not visited[y]:
            visited[y] = True
            distance[y] = distance[x] + cost
            dfs(y)


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, dst = map(int, input().split())
    graph[x].append((y, dst))
    graph[y].append((x, dst))

for _ in range(M):
    x, y = map(int, input().split())
    visited = [False for _ in range(N+1)]
    distance = [-1 for _ in range(N+1)]
    visited[x] = True
    distance[x] = 0
    dfs(x)
    print(distance[y])
