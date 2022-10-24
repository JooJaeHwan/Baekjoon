'''
문자열 반복
https://www.acmicpc.net/problem/2675
'''

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cnt, word = input().rstrip().split()
    for w in word:
        print(w*int(cnt), end='')

    print()
