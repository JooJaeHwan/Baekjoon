'''
소트인사이드
https://www.acmicpc.net/problem/1427
정렬
'''



import sys 

input = sys.stdin.readline

data = str(input().rstrip())

for i in range(9, -1, -1):
    for j in data:
        if int(j) == i:
            print(i, end='')