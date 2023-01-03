'''
Byte Coin
https://www.acmicpc.net/problem/17521
그리디 알고리즘
'''


import sys


input = sys.stdin.readline

n, W = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    if arr[i] < arr[i+1]:
        W = (W // arr[i]) * arr[i+1] + W % arr[i]

print(W)