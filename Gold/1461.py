'''
도서관
https://www.acmicpc.net/problem/1461
그리디 알고리즘, 정렬
'''


import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

positive = []
negative = []

largest = max(max(books), -min(books))
result = 0

for book in books:
    if book > 0:
        heapq.heappush(positive, -book)
    else:
        heapq.heappush(negative, book)

while positive:
    result += heapq.heappop(positive)
    for _ in range(M - 1):
        if positive:
            heapq.heappop(positive)
while negative:
    result += heapq.heappop(negative)
    for _ in range(M - 1):
        if negative:
            heapq.heappop(negative)

print(-result * 2 - largest)