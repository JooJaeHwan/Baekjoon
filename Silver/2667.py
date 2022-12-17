'''
단지번호붙이기
https://www.acmicpc.net/problem/2667
그래프 이론, 그래프 탐색, 깊이 우선 탐색, 넓이 우선 탐색
'''


import sys

input = sys.stdin.readline

dic = {0:[1, 0], 1:[-1, 0], 2:[0, 1], 3:[0, -1]}

def dfs(x, y):
    result = 1
    for i in range(4):
        nx = x + dic[i][0]
        ny = y + dic[i][1]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                result += dfs(nx, ny)
    return result

N = int(input())
graph = [[0] * N for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(N):
        graph[i][j] = int(row[j])

answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = -1
            answer.append(dfs(i, j))

answer.sort()
print(len(answer))
print('\n'.join(map(str, answer)))
