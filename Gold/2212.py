'''
센서
https://www.acmicpc.net/problem/2212
그리드 알고리즘, 정렬
'''


import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

if K >= N:
    print(0)
    sys.exit()

sensors = list(map(int, input().split()))
sensors.sort()

distance = []
for i in range(1, N):
    distance.append(sensors[i] - sensors[i - 1])

distance.sort()
for _ in range(K-1):
    distance.pop()

print(sum(distance))


