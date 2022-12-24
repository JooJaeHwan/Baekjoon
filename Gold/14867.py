'''
물통
https://www.acmicpc.net/problem/14867
자료구조, 그래프 이론, 그래프 탐색, 너비 우선 탐색
'''


import sys
from collections import deque


input = sys.stdin.readline


a, b, c, d = map(int, input().split())
def visit(q, visited, cnt, nx, ny):
    if (nx, ny) not in visited:
        q.append((cnt, nx, ny))
        visited.add((nx, ny))


def bfs(x, y):
    q = deque([(0, x, y)])
    visited = set()
    
    while q:
        cnt, a_value, b_value = q.popleft()
        if (a_value, b_value) == (c, d):
            return cnt
        nx, ny = a_value, 0       # Empty B
        visit(q, visited, cnt+1, nx, ny)
        nx, ny = 0, b_value       # Empty A
        visit(q, visited, cnt+1, nx, ny)
        nx, ny = a_value, b
        visit(q, visited, cnt+1, nx, ny)
        nx, ny = a, b_value
        visit(q, visited, cnt+1, nx, ny)
        # B에서 A로 물 옮기기
        if a_value + b_value < a:
            nx, ny = a_value + b_value, 0
        else:
            nx, ny = a, a_value + b_value - a
        visit(q, visited, cnt+1, nx, ny)
        # A에서 B로 물 옮기기
        if a_value + b_value < b:
            nx, ny = 0, a_value + b_value
        else:
            nx, ny = a_value + b_value - b, b 
        visit(q, visited, cnt+1, nx, ny)
    return -1

print(bfs(0, 0))