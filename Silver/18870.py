'''
좌표 압축
https://www.acmicpc.net/problem/18870
정렬, 값 / 좌표 압축
'''


import sys

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

set_array = list(set(array))

set_array.sort()

mapping = {num:idx for idx, num in enumerate(set_array)}

print(*[mapping[x] for x in array])