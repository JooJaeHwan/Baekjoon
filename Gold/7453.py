'''
합이 0인 네정수
https://www.acmicpc.net/problem/7453
정렬, 이분 탐색, 투 포인터, 중간에서 만나기
'''


import sys


input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []

for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

counter = {}
result = 0
for i in range(N):
    for j in range(N):
        sum_num = A[i] + B[j]
        if sum_num in counter:
            counter[sum_num] += 1
        else:
            counter[sum_num] = 1

for i in range(N):
    for j in range(N):
        sum_num = C[i] + D[j]
        if -sum_num in counter:
            result += counter[-sum_num]

print(result)