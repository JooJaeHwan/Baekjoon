'''
직사각형에서 탈출
https://www.acmicpc.net/problem/1085
'''


import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min([x, w-x, y, h-y]))


'''
6 2 10 3

1
'''