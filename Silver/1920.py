'''
수 찾기
https://www.acmicpc.net/problem/1920
'''


import sys

input = sys.stdin.readline

N = int(input())

N_list = set(map(int, input().split()))

M = int(input())

X = list(map(int, input().split()))

for i in X:
    if i not in N_list:
        print('0')
    else:
        print('1')