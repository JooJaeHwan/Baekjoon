'''
톱니바퀴
https://www.acmicpc.net/problem/14891
구현, 시뮬레이션
'''


import sys


input = sys.stdin.readline


def dfs(index, direction, rotation, move=True):
    if index <= 2  and direction == 'R':
        if gears[index][2] != gears[index + 1][6]:
            next_rotation = 'R'
            if rotation == 'R': next_rotation = 'L'
            dfs(index + 1, 'R', next_rotation)
    elif index >= 1 and direction == 'L':
        if gears[index][6] != gears[index - 1][2]:
            next_rotation = 'R'
            if rotation == 'R': next_rotation = 'L'
            dfs(index - 1, 'L', next_rotation)
    
    if move:
        rotate(index, rotation)

def rotate(index, rotation):
    result = [None] * 8
    if rotation == 'R':
        for i in range(8):
            result[(i + 1) % 8] = gears[index][i]
    if rotation == 'L':
        for i in range(8):
            result[(i - 1) % 8] = gears[index][i]
    gears[index] = result


gears = [[] for _ in range(4)]
for i in range(4):
    gear = input().strip()
    for j in range(len(gear)):
        gears[i].append(int(gear[j]))


K = int(input())
for i in range(K):
    index, rotation = map(int, input().split())
    index -= 1
    if rotation == 1:
        rotation = 'R'
    else:
        rotation = 'L'
    
    dfs(index, 'R', rotation, move=False)
    dfs(index, 'L', rotation)

result = 0
if gears[0][0] == 1:
    result += 1
if gears[1][0] == 1:
    result += 2
if gears[2][0] == 1:
    result += 4
if gears[3][0] == 1:
    result += 8

print(result)
