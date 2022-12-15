'''
두 수의 합
https://www.acmicpc.net/problem/3273
정렬, 투 포인터
'''


import sys


input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()

result = 0
start = 0
end = N - 1

while start < end:
    current = array[start] + array[end]
    if current == x:
        result += 1
        start += 1
    elif current < x:
        start += 1
    elif current > x:
        end -= 1
    
print(result)
