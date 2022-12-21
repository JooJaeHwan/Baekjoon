'''
트리
https://www.acmicpc.net/problem/4803
자료구조, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 분리 집합
'''


import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def is_cycle(x, prev):
    visited[x] = True

    for y in graph[x]:
        if visited[y]:
            if y != prev:
                return True
        else:
            if is_cycle(y, x):
                return True
    return False

T = 1
while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    
    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            if not is_cycle(i, 0):
                cnt += 1
    
    if cnt == 0:
        print(f'Case {T}: No trees.')
    elif cnt == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: A forest of {cnt} trees.')
    T += 1