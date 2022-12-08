'''
뒤집기
https://www.acmicpc.net/problem/1439
문자열, 그리드 알고리즘
'''


import sys

input = sys.stdin.readline

string = str(input().rstrip())

count0 = 0
count1 = 0

if string[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        if string[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
