'''
미로만들기
https://www.acmicpc.net/problem/2665
그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라
'''


import sys
import heapq

input = sys.stdin.readline


N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(N):
        graph[i][j] = int(row[j])
    
dic = {0:[1, 0], 1:[-1, 0], 2:[0, 1], 3:[0, -1]}
visited = [[-1 for _ in range(N)] for _ in range(N)]

def bfs(cnt, x, y):
    q = []
    heapq.heappush(q, (cnt, x, y))
    visited[x][y] = 0
    while q:
        cnt, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = cnt + 1
                    heapq.heappush(q, (cnt + 1, nx, ny))
                else:
                    visited[nx][ny] = cnt
                    heapq.heappush(q, (cnt, nx, ny))

bfs(0, 0, 0)
print(visited[N - 1][N - 1])