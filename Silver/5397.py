'''
키로거
https://www.acmicpc.net/problem/5397
'''


import sys

input = sys.stdin.readline

L = int(input())

for _ in range(L):
    password = input().strip()
    left_stack = []
    right_stack = []
    for p in [*password]:
        if p == '-':
            if left_stack:
                left_stack.pop()
        elif p == "<":
            if left_stack:
                right_stack.append(left_stack.pop())

        elif p == '>':
            if right_stack:
                left_stack.append(right_stack.pop())

        else:
            left_stack.append(p)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))