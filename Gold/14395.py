'''
4연산
https://www.acmicpc.net/problem/14395
그래프 이론, 그래프 탐색, 너비 우선 탐색
'''


import sys
from collections import deque

input = sys.stdin.readline


A, B = map(int, input().split())


def bfs(x):
    q = deque([(x, '')])
    visited = set([x])
    while q:
        now, opers = q.popleft()
        if now > int(1e9):
            continue
        if now == B:
            return opers
        for oper in ['*', '+', '-', '/']:
            if oper == '*':
                next = now * now
            elif oper == '+':
                next = now + now
            elif oper == '-':
                next = now - now
            elif oper == '/':
                next = 1
            if next not in visited:
                q.append((next, opers + oper))
                visited.add(next)
    
    return -1

if A == B:
    print(0)
    sys.exit(0)
print(bfs(A))
