'''
랜선 자르기
https://www.acmicpc.net/problem/1654
'''


import sys

input = sys.stdin.readline

k, n = map(int, input().split())
data = []

for _ in range(k):
    data.append(int(input()))

start = 1
end = max(data)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += data[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)


'''
4 11
802
743
457
539
-----
200
'''