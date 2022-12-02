'''
우주신과의 교감
https://www.acmicpc.net/problem/1774
그래프 이론, 최소 스패닝 트리
'''


import sys
import math

input = sys.stdin.readline


def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a ** 2) + (b ** 2))

def get_parent(parent, n):
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n])

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False


edges = []
parent = {}
locations = []
N, M = map(int, input().split())
for _ in range(N):
    x, y = map(int, input().split()) 
    locations.append((x, y))


length = len(locations)

for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))


for i in range(1, N + 1):
    parent[i] = i
for i in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
    if not find_parent(parent, a, b): 
        union_parent(parent, a, b) 
        result += cost

print("%0.2f" % result)