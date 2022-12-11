'''
시리얼 번호
https://www.acmicpc.net/problem/1431
정렬
'''


import sys

input = sys.stdin.readline

N = int(input())

array = []
def digit_sum(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result


for _ in range(N):
    array.append(str(input().rstrip()))


array.sort(key=lambda x: (len(x), digit_sum(x), x))

print('\n'.join(array))