'''
K 번째 수
https://www.acmicpc.net/problem/11004
정렬
'''


import sys

input = sys.stdin.readline

N, K = map(int, input().split())

A = list(map(int, input().split()))

A.sort()

print(A[K-1])