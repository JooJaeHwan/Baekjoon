'''
회전하는 큐
https://www.acmicpc.net/problem/1021
'''

import sys 
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

targets = list(map(int, input().split()))

q = deque([i for i in range(1, N + 1)])
cnt = 0

for target in targets:
    idx = q.index(target)
    if idx <= len(q) // 2:
        for i in range(idx):
            q.rotate(-1)
            cnt += 1
    else:
        for i in range(len(q) - idx):
            q.rotate(1)
            cnt += 1
    q.popleft()
print(cnt)