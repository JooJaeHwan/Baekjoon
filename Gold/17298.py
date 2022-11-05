'''
오큰수
https://www.acmicpc.net/problem/17298
'''


import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))
stack = []
answer = [-1] * N
for i in range(len(data)):
    while stack and data[stack[-1]] < data[i]:
            answer[stack.pop()] = data[i] 
            
    stack.append(i) 

print(*answer) 
