'''
베스트셀러
https://www.acmicpc.net/problem/1302
자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵
'''


import sys

input = sys.stdin.readline

N = int(input())

books = {}

for _ in range(N):
    book = str(input().strip())
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

target = max(books.values())
result = []

for book, number in books.items():
    if number == target:
        result.append(book)
    
print(sorted(result)[0])
