'''
전화번호 목록
https://www.acmicpc.net/problem/5052
자료구조, 문자열, 정렬, 트리, 트라이
'''


import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    array = []

    for _ in range(N):
        array.append(input().strip())
    
    array.sort()
    result = False
    for i in range(N - 1):
        if len(array[i]) < len(array[i + 1]):
                if array[i] == array[i + 1][:len(array[i])]:
                    result = True
                    break
    if result:
        print("NO")
    else:
        print("YES")