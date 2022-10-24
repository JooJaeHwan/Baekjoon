'''
ATM
https://www.acmicpc.net/problem/11399
'''



import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
num = 0
S.sort()

for i in range(N):
    for j in range(i+1):
        num += S[j]

print(num)