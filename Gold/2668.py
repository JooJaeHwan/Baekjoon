'''
숫자고르기
https://www.acmicpc.net/problem/2668
그래프 이론, 그래프 탐색, 깊이 우선 탐색
'''


import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = True
    y = graph[x]

    if not visited[y]:
        dfs(y)
    
    elif not finished[y]:
        while y != x:
            result.append(y)
            y = graph[y]
        result.append(x)

    finished[x] = True
    

N = int(input())
graph = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
finished = [False for _ in range(N + 1)]
result = []

for i in range(1, N + 1):
    graph[i] = int(input())

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

print(len(result))
print('\n'.join(map(str, sorted(result))))