'''
이장님 초대
https://www.acmicpc.net/problem/9237
그리디 알고리즘, 정렬
'''


import sys

input = sys.stdin.readline

N = int(input()) # 나무 묘목의 수

arr = list(map(int, input().split())) # 묘목이 자라는데 걸리는 시간
arr.sort(reverse=True) # 내림차순으로 정렬

max_value = 0

for i in range(N):
    max_value = max(max_value, i + 1 + arr[i])

print(max_value + 1)