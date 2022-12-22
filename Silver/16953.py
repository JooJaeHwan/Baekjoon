'''
A → B
https://www.acmicpc.net/problem/16953
그래프 이론, 그리디 알고리즘, 그래프 탐색, 너비 우선 탐색
'''


import sys
from collections import deque

input = sys.stdin.readline


A, B = map(int, input().split())


def bfs(x):
    q = deque([(x, 1)])

    while q:
        now, cnt = q.popleft()
        if now == B:
            return cnt
        elif now < B:
            cnt += 1
            q.append((now*2, cnt))
            q.append((now*10 + 1, cnt))
        else: continue
    
    return -1

print(bfs(A))


