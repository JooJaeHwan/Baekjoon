'''
풍선 터뜨리기
https://www.acmicpc.net/problem/2346
'''


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque(enumerate(map(int, input().split())))
stack = []

while q:
    idx, num = q.popleft()
    stack.append(idx + 1)
    if num > 0:
        q.rotate(-(num - 1))
    elif num < 0:
        q.rotate(-num)
print(' '.join(map(str, stack)))