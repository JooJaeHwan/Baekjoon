'''
상어 초등학교
https://www.acmicpc.net/problem/21608
'''


import sys

input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N**2)]
dic = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}

for student in students:
    tmp = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr = r + dic[k][0]  
                    nc = c + dic[k][1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, r, c])
    ### !!!! like, blank는 클 수록, 행과 열의 수는 작을수록 답이니 lambda 뒤의 조건을 잘 줘야함!!!
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    ### 정렬 후 젤 앞에 있는 리스트의 행과 열의 번호에 학생 앉히기 
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함 
students.sort()

for r in range(N):
    for c in range(N):
        ans = 0
        for k in range(4):
            nr = r + dic[k][0]  
            nc = c + dic[k][1]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] in students[arr[r][c]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)