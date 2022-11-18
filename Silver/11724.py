'''
연결 요소의 개수
https://www.acmicpc.net/problem/11724
'''


import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())

parent = [0] * (N+1)

for i in range(N):
    parent[i] = i

for i in range(M):
    x, y = map(int, input().split())
    union_parent(parent, x, y)

counter = []
for i in range(1, N+1):
    counter.append(find_parent(parent, i))

print(len(set(counter)))