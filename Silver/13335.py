'''
트럭
https://www.acmicpc.net/problem/13335
'''


import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
data = deque(list(map(int, input().split())))

bridge = deque([0] * w)
time = 0

while bridge:
    time += 1
    bridge.popleft()
    if data:
        if sum(bridge) + data[0] <= L:
            bridge.append(data.popleft())
        else:
            bridge.append(0)
print(time)

