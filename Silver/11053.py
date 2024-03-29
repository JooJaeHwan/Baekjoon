'''
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
'''

import sys

input = sys.stdin.readline

N = int(input())

A_list = list(map(int, input().split()))

dp = [1] * N 

for i in range(1, N):
    for j in range(i):
        if A_list[j] < A_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
