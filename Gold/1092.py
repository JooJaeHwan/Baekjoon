'''
배
https://www.acmicpc.net/problem/1092
그리디 알고리즘, 정렬
'''


import sys

input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

position = [0] * N
checked = [False] * M

cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0

while True:
    if count == len(boxes):
        break
    for i in range(N):
        while position[i] < len(boxes):
            if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
                checked[position[i]] = True
                position[i] += 1
                count += 1
                break
            position[i] += 1
    result += 1
print(result)