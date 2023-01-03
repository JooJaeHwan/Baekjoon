'''
주식
https://www.acmicpc.net/problem/11501
그리디 알고리즘
'''


import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[-1]
    target = [0] * N

    for i in range(N - 1, -1, -1):
        max_value = max(max_value, arr[i])
        target[i] = max_value
    
    result = 0
    for i in range(N):
        result += max(0, target[i] - arr[i])
    
    print(result)