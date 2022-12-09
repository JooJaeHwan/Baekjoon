'''
N-Queen
https://www.acmicpc.net/problem/9663
브루트포스 알고리즘, 백트래킹
'''


import sys

input = sys.stdin.readline

N = int(input())
row = [0] * N
result = 0

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                dfs(x+1)
    return result

print(dfs(0))