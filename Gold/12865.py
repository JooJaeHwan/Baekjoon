'''
평범한 배낭
https://www.acmicpc.net/problem/12865
다이나믹 프로그래밍, 배낭 문제
'''


import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, input().split())
    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)

print(dp[N][K])


