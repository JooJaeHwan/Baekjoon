'''
LCS
https://www.acmicpc.net/problem/9251
다이나믹 프로그래밍, 문자열
'''


import sys

input = sys.stdin.readline

word_1 = str(input().strip())
word_2 = str(input().strip())


dp = [[0] * (len(word_2) + 1) for _ in range(len(word_1) + 1)]

for i in range(1, len(word_1) + 1):
    for j in range(1, len(word_2) + 1):
        if word_1[i - 1] == word_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len(word_1)][len(word_2)])