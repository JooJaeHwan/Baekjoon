'''
0 만들기
https://www.acmicpc.net/problem/7490
재귀 함수
'''


import sys
import copy

input = sys.stdin.readline


def recursive(array, N):
    if len(array) == N:
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, N)
    array.pop()

    array.append('+')
    recursive(array, N)
    array.pop()

    array.append('-')
    recursive(array, N)
    array.pop()


T = int(input())

for _ in range(T):
    operators_list = []
    N = int(input())
    recursive([], N - 1)

    integers =[i for i in range(1, N + 1)]

    for operators in operators_list:
        string = ''
        for i in range(N - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()




    
