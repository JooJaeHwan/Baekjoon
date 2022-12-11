'''
보물
https://www.acmicpc.net/problem/1026
수학, 그리디 알고리즘, 정렬
'''



import sys


input = sys.stdin.readline


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

result = 0

for i in range(N):
    result += (A[i] * B[i])

print(result)