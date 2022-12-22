'''
물통
https://www.acmicpc.net/problem/14867
자료구조, 그래프 이론, 그래프 탐색, 너비 우선 탐색
'''


import sys
from collections import deque


input = sys.stdin.readline


a, b, c, d = map(int, input().split())

def bfs(x, y):
    q = deque([(0, x, y)])
    visited = set()
    
    while q:
        cnt, a_value, b_value = q.popleft()
        if (a_value, b_value) == (c, d):
            return cnt
        if a_value == a:
            q.append((0, b_value))

