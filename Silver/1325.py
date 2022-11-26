'''
효율적인 해킹
https://www.acmicpc.net/problem/1325
그래프 이론, 그래프 탐색, 넓이 우선 탐색, 깊이 우선 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, input().split())
    adj[Y].append(X)

def bfs(v):
    q = deque([v])
    visited = [False] * (N + 1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for i in adj[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count += 1
    return count

result = []
max_value = -1

for i in range(1, N + 1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

print(' '.join(map(str, result)))



