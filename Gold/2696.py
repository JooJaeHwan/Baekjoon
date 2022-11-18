'''
중앙값 구하기
https://www.acmicpc.net/problem/2696
자료구조, 우선순위 큐
'''

import sys 
import heapq


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    data = []
    right =[]
    left = []

    if M % 10 == 0:
        for _ in range(M // 10):
            data.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(M // 10 + 1):
            data.extend(list(map(int, input().rstrip().split())))

    mid = data[0]
    result = [mid]

    for idx, val in enumerate(data[1:], 1):
        if mid > val:
            heapq.heappush(left, -val)
        else:
            heapq.heappush(right, val)
        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            result.append(mid)
    print(len(result))
    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()



    