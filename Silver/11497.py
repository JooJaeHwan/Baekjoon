'''
통나무 건너뛰기
https://www.acmicpc.net/problem/11497
그리디 알고리즘, 정렬
'''

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    
    result = [0] * N
    result[N // 2] = data[0]
    for i in range(1, N):
        if i % 2 == 1:
            result[N // 2 - i // 2 - 1] = data[i]
        else:
            result[N // 2 + i // 2] = data[i]

    max_dif = 0
    for i in range(N):
        dif = abs(result[i] - result[(i + 1) % N])
        max_dif = max(max_dif, dif)
    print(max_dif)
