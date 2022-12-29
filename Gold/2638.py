'''
치즈
https://www.acmicpc.net/problem/2638
구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션, 깊이 우선 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
dic = {0 : [1, 0], 1 : [-1, 0], 2 : [0, 1], 3 : [0, -1]}

def bfs():
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True

def melt():
    finish = True
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                finish = False
            elif graph[i][j] == 2:
                graph[i][j] = 1
    return finish

result = 0

while True:
    bfs()
    if melt():
        print(result)
        break
    else:
        result += 1