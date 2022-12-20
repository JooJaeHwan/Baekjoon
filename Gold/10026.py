'''
적록색약
https://www.acmicpc.net/problem/10026
그래프 이론, 그래프 탐색, 깊이 우선 탐색, 넓이 우선 탐색
'''


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dic = {0:[1, 0], 1:[-1, 0], 2:[0, 1], 3:[0, -1]}

def dfs(ver, x, y):
    if ver == 0:
        tmp = graph[x][y]
        visited[x][y] = True
        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == tmp:
                    visited[nx][ny] = True
                    dfs(0, nx, ny)
    else:
        tmp = graph[x][y]
        visited[x][y] = True
        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if tmp == 'R' or tmp == 'G':
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        visited[nx][ny] = True
                        dfs(1, nx, ny)
                else:
                    if graph[nx][ny] == tmp:
                        visited[nx][ny] = True
                        dfs(1, nx, ny)

N = int(input())
graph = [[0] * N for _ in range(N)]
result = []
color = 0

for i in range(N):
    row = input().strip()
    for j in range(N):
        graph[i][j] = row[j]

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color += 1
            dfs(0, i, j)
result.append(color)

visited = [[False] * N for _ in range(N)]
color = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color += 1
            dfs(1, i, j)
result.append(color)

print(*result)
