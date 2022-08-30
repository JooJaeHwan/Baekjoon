'''
평균
https://www.acmicpc.net/problem/1546
'''

import sys

input = sys.stdin.readline

n = int(input())
data = (list(map(int, input().split())))

print(sum(data)/max(data)*100/n)



'''
3
40 80 60
-------
75.0
'''