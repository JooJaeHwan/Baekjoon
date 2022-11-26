'''
숨바꼭질
https://www.acmicpc.net/problem/1697
그래프 이론, 그래프 탐색, 넓이 우선 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
array = [0] * MAX

def bfs():
    q = deque([N])
    while q:
        now_pos = q.popleft()
        if now_pos == K:
            return array[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)
print(bfs())
