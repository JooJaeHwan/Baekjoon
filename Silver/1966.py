'''
프린터 큐
https://www.acmicpc.net/problem/1966
'''

import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    cnt = 0
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == M:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


