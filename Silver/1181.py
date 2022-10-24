'''
단어 정렬
https://www.acmicpc.net/problem/1181
'''

import sys

input = sys.stdin.readline

N = int(input())
data = []

for _ in range(N):
    data.append(input().strip())

set_data = set(data)
data = list(set_data)
data.sort()
data.sort(key = len)

for d in data:
    print(d)


'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
--------
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''

    