'''
문서 검색
https://www.acmicpc.net/problem/1543
문자열, 브루트포스 알고리즘
'''

import sys

input = sys.stdin.readline

document = str(input().strip())
word = str(input().strip())

idx = 0
result = 0

while len(document) - idx >= len(word):
    if document[idx:idx + len(word)] == word:
        result += 1
        idx += len(word)
    else:
        idx += 1

print(result)