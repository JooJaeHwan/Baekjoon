'''
나는 요리사다
https://www.acmicpc.net/problem/2953
'''



import sys

input = sys.stdin.readline
max_value = 0
result = 0


for i in range(1, 6):
    data = list(map(int, input().split()))
    sum_data = sum(data)

    if max_value < sum_data:
        max_value = sum_data
        result = i

print(result, max_value)
