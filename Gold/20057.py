'''
마법사 상어와 토네이도
https://www.acmicpc.net/problem/20057
'''


import sys

# 서, 남, 동, 북 방향 정보
dic = {0: [0, -1], 1:[1, 0], 2:[0, 1], 3:[-1, 0]}

# 방향별 모래 비율
left = [(-2, 0, 0.02), (-1, -1, 0.10), (-1, 0, 0.07),
        (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.10),
        (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)]
down = [(-y, x, val) for x, y, val in left]
right = [(x, -y, val) for x, y, val in left]
up = [(y, x, val) for x, y, val in left]
ratio = [left, down, right, up]

def move():
    global x, y, direction, turned, moved, target
    if moved == target: # 충분히 이동했다면 회전 수행
        moved = 0
        turned += 1
        direction = (direction + 1) % 4
    if turned == 2: # 2번 회전했다면, 이동할 칸 수 증가
        turned = 0
        target += 1
    
    # 다음 위치로 이동
    x = x + dic[direction][0]
    y = y + dic[direction][1]
    moved += 1

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

x = N // 2
y = N // 2
direction = 0 # 방향 (처음에 서쪽)
turned = 0 # 회전한 횟수
moved = 0 # 현재 방향으로 이동한 수
target = 1 # 이동할 칸 수
result = 0 # 맵을 벗어나는 모래의 양
cnt = 1 # 총 이동 횟수

while cnt < N * N:
    move() # 한 칸 이동
    remain = arr[x][y] # 남은 모래양 
    for i in range(9): # 각 9개의 위치로 모래 옮기기
        nx, ny, percentage = ratio[direction][i]
        nx += x
        ny += y
        current = int(arr[x][y] * percentage) # 옮길 모래 양

        # 맵을 벗어나는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            result += current
        else:
            arr[nx][ny] += current
        remain -= current
    
    # 알파 값 처리하기 (남은 모래 옮기기)
    nx = x + dic[direction][0]
    ny = y + dic[direction][1]

    # 맵을 벗어나는 경우
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        result += remain
    else:
        arr[nx][ny] += remain
    arr[x][y] = 0
    cnt += 1
print(result)
