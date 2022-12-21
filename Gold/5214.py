'''
환승
https://www.acmicpc.net/problem/5214
그래프 이론, 그래프 탐색, 넓이 우선 탐색
'''


import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())
graph = [[] for _ in range(N + M + 1)]

for i in range(1, M + 1):
    data = list(map(int, input().split()))
    for x in data:
        graph[x].append(N + i)
        graph[N + i].append(x)

visited = set([1])
q = deque([(0, 1)])
found = False

while q:
    cost, now = q.popleft()
    if now == N:
        print(cost // 2 + 1)
        found = True
        break
    for y in graph[now]:
        if y not in visited:
            q.append((cost+1, y))
            visited.add(y)

if not found:
    print(-1)  