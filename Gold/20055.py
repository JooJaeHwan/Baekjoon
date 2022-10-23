'''
컨베이어 벨트 위의 로봇
https://www.acmicpc.net/problem/20055
'''


import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False] * N)
result = 1

while True: 

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate()
    robot.rotate()
    robot[N - 1] = False # 내리는 위치에서 로봇 내리기
    
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다,
    # 만약 이동할 수 없다면 가만히 있는다.
    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] >= 1:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1
    robot[N - 1] = False # 내리는 위치에서 로봇 내리기

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면, 올리는 위치에 로봇을 올린다.
    if belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1
    
    # 4. 내구도 0이 K개 이상이라면 종료
    if belt.count(0) >= K:
        break
    result += 1
print(result)