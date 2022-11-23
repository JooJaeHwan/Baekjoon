'''
가장높은탑쌓기
https://www.acmicpc.net/problem/2655
다이나믹 프로그래밍
'''

import sys

input = sys.stdin.readline

N = int(input())

stones = []

stones.append((0, 0, 0, 0))
for i in range(1, N + 1):
    area, height, weight = map(int, input().split())
    stones.append((i, area, height, weight))

stones.sort(key=lambda x: x[3])

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if stones[i][1] > stones[j][1]:
            dp[i] = max(dp[i], dp[j] + stones[i][2])

max_value = max(dp)
idx = N
result = []

while idx != 0:
    if max_value == dp[idx]:
        result.append(stones[idx][0])
        max_value -= stones[idx][2]
    idx -= 1

result.reverse()
print(len(result))
print('\n'.join(map(str, result)))

