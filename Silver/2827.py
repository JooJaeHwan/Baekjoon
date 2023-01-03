'''
우리집에 도서관이 있어
https://www.acmicpc.net/problem/2872
그리디 알고리즘
'''

import sys

input = sys.stdin.readline


N = int(input())
books = []

for _ in range(N):
    books.append(int(input()))


max_value = 0
max_index = -1

for idx, book in enumerate(books):
    if max_value < book:
        max_value = book
        max_index = idx


length = 1
target = max_value - 1

for i in range(max_index - 1, -1, -1):
    if target == books[i]:
        target -= 1
        length += 1

print(N - length)