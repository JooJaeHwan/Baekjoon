'''
연구소3
https://www.acmicpc.net/problem/17142
'''


import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
inf = sys.maxsize

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(active):
    q = deque()
    dic = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}
    visited = [[-1] * N for _ in range(N)]
    result = 0

    for x, y in active:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dic[i][0]  
            ny = y + dic[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0  and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    result = max(result, visited[nx][ny])
                elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    if list(sum(visited, [])).count(-1) != wall_cnt:
        return inf
    return result

wall_cnt = 0
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            wall_cnt += 1
        elif graph[i][j] == 2:
            virus.append((i, j))

ans = inf
for active in combinations(virus, M):
    ans = min(ans, bfs(active))

print(ans if ans != inf else -1)