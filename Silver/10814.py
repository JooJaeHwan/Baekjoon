'''
나이순 정렬
https://www.acmicpc.net/problem/10814
정렬
'''


import sys

input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    age, name = map(str, input().rstrip().split())
    result.append((age, name))

result.sort(key=lambda x: int(x[0]))

for i in result:
    print(' '.join(i))