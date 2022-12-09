'''
암호 만들기
https://www.acmicpc.net/problem/1759
수학, 브루트포스 알고리즘, 조합론, 백트래킹
'''


import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
data = list(map(str, input().rstrip().split()))
data.sort()

for combi in combinations(data, L):
    count = 0
    for i in combi:
        if i in vowels:
            count += 1
    if count >= 1 and count <= L - 2:
        print(''.join(combi))