'''
유기농 배추
https://www.acmicpc.net/problem/1012
그래프 이론, 그래프 탐색, 넓이 우선 탐색, 깊이 우선 탐색
'''


import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

T = int(input())

def dfs(x, y):
    visited[x][y] = True
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0<= ny < M:
            if array[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int, input().split()) 
    array = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        Y, X = map(int, input().split())
        array[X][Y] = 1
    result = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)


