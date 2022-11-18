'''
주사위
https://www.acmicpc.net/problem/1233
'''


import sys

input =  sys.stdin.readline

S1, S2, S3 = map(int, input().split())

num_list = [0] * (S1 + S2 + S3 + 1)

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            num_list[i+j+k] += 1
print(num_list.index(max(num_list)))
