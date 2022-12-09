'''
알파벳
https://www.acmicpc.net/problem/1987
그래프 이론, 그래프 탐색, 넓이 우선 탐색, 백트래킹
'''

import sys

input = sys.stdin.readline

R, C = map(int, input().split())
dic = {0:[0, 1], 1: [0, -1], 2:[1, 0], 3: [-1, 0]}
array = []

result = 0

for _ in range(R):
    array.append(str(input().rstrip()))

def bfs(x, y):
    global result

    q = set()
    q.add((x, y, array[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            if 0 <= nx < R and 0 <= ny < C and array[nx][ny] not in step:
                q.add((nx, ny, step + array[nx][ny]))
    return result

print(bfs(0, 0))    
