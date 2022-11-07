'''
요세푸스 문제 0
https://www.acmicpc.net/problem/11866
'''


import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)])
stack = []

while q:
    q.rotate(-(K-1))
    stack.append(q.popleft())

print("<"+ ', '.join(map(str, stack)) + ">")
