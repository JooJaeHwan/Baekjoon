'''
사이클 게임
https://www.acmicpc.net/problem/20040
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

parent = [0] * N

for i in range(N):
    parent[i] = i

cycle =False
for i in range(M):
    x, y = map(int, input().split())

    if find_parent(parent, x) == find_parent(parent, y):
        cycle = True
        print(i+1)
        break
    else:
        union_parent(parent, x, y)
if not cycle:
    print(0)