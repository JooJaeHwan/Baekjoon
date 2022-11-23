'''
기타리스트
https://www.acmicpc.net/problem/1495
다이나믹 프로그래밍
'''


import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())

volums = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

dp[0][S] = 1

for i in range(1, N + 1):
    for j in range(M + 1):
        if dp[i - 1][j] == 0:
            continue
        if j - volums[i - 1] >= 0:
            dp[i][j - volums[i - 1]] = 1
        if j + volums[i - 1] <= M:
            dp[i][j + volums[i - 1]] = 1

result = -1

for i in range(M, -1, -1):
    if dp[N][i] == 1:
        result = i
        break

print(result)
