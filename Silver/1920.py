'''
수 찾기
https://www.acmicpc.net/problem/1920
'''


import sys

input = sys.stdin.readline

N = int(input())

N_list = list(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))

N_list.sort()

def binary(i):
    first = 0
    end = N - 1

    while first <= end:
        mid = (first + end) // 2
        if N_list[mid] == i:
            return True
        if i < N_list[mid]:
            end = mid - 1
        elif i > N_list[mid]:
            first = mid + 1


for i in range(M):
    if binary(M_list[i]):
        print(1)
    else:
        print(0)