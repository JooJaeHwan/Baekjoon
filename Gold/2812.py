'''
크게 만들기
https://www.acmicpc.net/problem/2812
자료 구조, 그리디 알고리즘, 스택
'''


import sys


input = sys.stdin.readline


N, K = map(int, input().split())
numbers = input().strip()

stack = []
cnt = 0


for number in numbers:
    while stack and stack[-1] < number and cnt != K:
        stack.pop()
        cnt += 1
    stack.append(number)

for i in range(K - cnt):
    stack.pop()

print(''.join(stack))