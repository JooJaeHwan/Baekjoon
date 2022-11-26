'''
바이러스
https://www.acmicpc.net/problem/2606
그래프 이론, 그래프 탐색, 넓이 우선 탐색, 깊이 우선 탐색
'''


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
T = int(input())

adj = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(T):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

def bfs(n):
    q = deque([n])
    while q:
        n = q.popleft()
        if visited[n] == 0:
            visited[n] = 1
            for i in adj[n]:
                if visited[i] == 0:
                    q.append(i)
    return sum(visited) - 1
print(bfs(1))


'=============================================='
visited = [0] * (N + 1)
def dfs(n):
    visited[n] = 1
    for next in adj[n]:
        if visited[next] == 0:
            dfs(next)
dfs(1)
print(sum(visited) - 1)
