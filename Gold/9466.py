'''
텀 프로젝트
https://www.acmicpc.net/problem/9466
그래프 이론, 그래프 탐색, 깊이 우선 탐색
'''


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

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


for _ in range(T):
    N = int(input())
    visited = [False for _ in range(N+1)]
    finished = [False for _ in range(N+1)]
    graph = [0] + list(map(int, input().split()))
    result = []

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)

    print(N - len(result))