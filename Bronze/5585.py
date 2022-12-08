'''
거스름돈
https://www.acmicpc.net/problem/5585
그리디 알고리즘
'''


import sys

input = sys.stdin.readline

pay = int(input())

charge = 1000 - pay

coin_types = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coin_types:
    count += charge // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    charge %= coin

print(count)
    