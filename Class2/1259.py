'''
팰린드롬수
https://www.acmicpc.net/problem/1259
'''


while True:
    num = input()
    if num == '0':
        break
    if num[::-1] == num:
        print('yes')
    else:
        print('no')


'''
121
1231
12421
0
--------
yes
no
yes
'''